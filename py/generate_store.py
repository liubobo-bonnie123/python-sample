#!/usr/bin/python2.6

##################################################################
# Generates a static store page; should be called once a month via
# cron and/or when the database is updated. The static store page 
# that is generated should then be displayed by display_store,
# which fills in button states.
##################################################################

from lxml import etree
from lxml.html.builder import *

import tempfile
import os
import errno
from copy import deepcopy
import db_connect
import builders
import datautils
import params
import errors
import config as c

from textutils import makeunicode, makecleanelement, trimtext
from efactory import CLASS, SRC, HREF, ID

TEMP_BASE = "/var/www/tmp/"
STORE_BASE = "/var/www/html/%s_store_base.html"
LEGACY_BASE = "/var/www/hearst-store/%s/index.html"

def main(store_id):
  # Get the store name and bundle id from the store dictionary.
  assert type(store_id) == int
  if store_id in c.STORES:
    bundle_id = c.STORES[store_id][0]
    template_name = c.STORES[store_id][1]
    store_name = c.STORES[store_id][2]
  else:
    raise errors.StoreError()

  # Bring in the HTML template.
  parser = etree.HTMLParser()
  HTMLtree = etree.parse("/var/www/html/"+template_name+"_template.html", parser)
  legacyHTMLtree = etree.parse("/var/www/html/legacy_"+template_name+"_template.html", parser)


  # Create db connection for fetching promotions.
  db = db_connect.open_cms_db()
  
  # Create and make query to retrieve data for the currently stored issues.
  db.db_cursor.execute("""
    SELECT *
    FROM content_items
    WHERE bundle_id = %s
    ORDER BY publication_date DESC
  """, (bundle_id,))
  items_results = db.db_cursor.fetchall()
  
  # Create and make query to retrieve preview image urls.
  db.db_cursor.execute("""SELECT content_item_id, image_url FROM previews""")
  previews_results = db.db_cursor.fetchall()
  
  # Close db connection.
  db.db_handle.close()


  # Create a workable dictionary of the preview image query.
  previews_dict = datautils.workablepreviews(previews_results)

  # Pop off the first item in the result as the featured item.
  featured_item = datautils.singleissue(items_results.pop(0), previews_dict)
  
  # Get a list of objects from the result, allowing the issue metadata to be 
  # accessed by name rather than index in the query results.
  previous_issues = datautils.listissues(items_results, previews_dict)


  # Find the featured section:
  featured_holder = HTMLtree.find(".//div[@id='featured_issue']")
  
  # Find the preview section:
  issue_holder = HTMLtree.find(".//div[@id='issue_float_holder']")
  
  # Find the lightbox section:
  details_holder = HTMLtree.find(".//div[@id='hide_details']")


  # Build the featured issue section.
  featured_id = str(featured_item.info["id"])

  if featured_item.info["price_tier"] > 0:
    featured_action_string = "Buy $"+str(float(featured_item.info["price_tier"]) - 0.01)
    featured_action_class = "buy_button"
  else:
    featured_action_string = "Download"
    featured_action_class = "purchased_button"

  featured_holder.append(
    A(
      IMG(
        ID("featured_cover"),
        SRC(featured_item.info["cover_url"])
      ),
      HREF("#frame"+featured_id),
      CLASS("show_lightbox")
    )
  )
  
  if featured_item.info["subtitle"] is not None:
    featured_subtitle = makecleanelement("<p>",featured_item.info["subtitle"],"</p>")
  else:
    featured_subtitle = makecleanelement("<p>","","</p>")  

  featured_holder.append(
    DIV(
      DIV(
        H1(makeunicode(featured_item.info["title"])),
        featured_subtitle,
        ID("featured_desc")
      ),
      DIV(
        A(
          DIV(
            featured_action_string,
            CLASS("feature_button","action_button",featured_action_class)
          ),
          HREF("sm://itemOpen/"+featured_id),
          CLASS("item"+featured_id)
        ),
        A(
          DIV(
            "Details",
            CLASS("feature_button","action_button","details_button")
          ),
          HREF("#frame"+featured_id),
          CLASS("show_lightbox")
        ),
        ID("featured_buttons")
      ),
      ID("featured_details")
    )
  )
  
  details_holder.append(builders.buildlightbox(featured_item, featured_action_string, featured_action_class))
  

  # Build the list of previous issues and the detail panels for each.  
  for issue in previous_issues:
    previous_id = str(issue.info["id"])

    if issue.info["price_tier"] > 0:
      issue_action_string = "Buy $"+str(float(issue.info["price_tier"]) - 0.01)
      issue_action_class = "buy_button"
    else:
      issue_action_string = "Download"
      issue_action_class = "purchased_button"
  
    # Append an issue element to the main scrollable list of previous issues.
    issue_holder.append(
      DIV(
        DIV(
          A(
            IMG(SRC(issue.info["thumbnail_url"])),
            HREF("#frame"+previous_id),
            CLASS("show_lightbox")
          ),
          CLASS("picture")
        ),
        DIV(makeunicode(trimtext(issue.info["title"], 20)), CLASS("desc_picture")),
        DIV(
          A(
            DIV(
              issue_action_string,
              CLASS("left_button","action_button",issue_action_class)
            ),
            HREF("sm://itemOpen/"+previous_id),
            CLASS("item"+previous_id)
          ),
          A(
            DIV(
              "Details",
              CLASS("right_button","action_button","details_button")
            ),
            HREF("#frame"+previous_id),
            CLASS("show_lightbox")
          ),
          CLASS("button_holder")          
        ),
        CLASS("issue")
      )
    )
    
    details_holder.append(builders.buildlightbox(issue, issue_action_string, issue_action_class))


  # Build out the legacy page.
  legacy_body = legacyHTMLtree.find(".//body")

  legacy_body.append(deepcopy(featured_holder))

  legacy_prev = etree.SubElement(legacy_body, "div")
  legacy_prev.set("id","previous_issues")
  legacy_scrl = etree.SubElement(legacy_prev, "div")
  legacy_scrl.set("id","scrollable")
  legacy_scrl.append(deepcopy(issue_holder))

  legacy_body.append(deepcopy(details_holder))


  # Write the generated HTML to a temporary file. Using temporary files prevents race conditions.
  data = etree.tostring(HTMLtree)
  tmp = tempfile.mkstemp(dir=TEMP_BASE)
  legacy_data = etree.tostring(legacyHTMLtree)
  legacy_tmp = tempfile.mkstemp(dir=TEMP_BASE)

  bytes_written = os.write(tmp[0], data)
  os.write(legacy_tmp[0], legacy_data)
  os.close(tmp[0])
  os.close(legacy_tmp[0])

  # Move the temporary file to the final URL.
  os.chmod(tmp[1], 0644)
  os.rename(tmp[1], STORE_BASE % (store_name))
  
  os.chmod(legacy_tmp[1], 0644)
  # Check if the target directory exists. If not, create it before writing.
  try:
    os.rename(legacy_tmp[1], LEGACY_BASE % (store_name))
  except OSError as e:
    if e.errno == errno.ENOENT:
      os.mkdir("/var/www/hearst-store/%s" % (store_name), 0777)
      os.rename(legacy_tmp[1], LEGACY_BASE % (store_name))
    else:
      raise e

  return bytes_written