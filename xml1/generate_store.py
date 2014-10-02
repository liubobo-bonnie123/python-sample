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
import db_connect
import builders
import datautils
import params
import errors
import config as c

from textutils import makeunicode, makecleanelement, trimtext
from efactory import CLASS, SRC, HREF, ID

# FIXME : for development/testing only
import cgi, cgitb
cgitb.enable()

TEMP_BASE = "/var/www/tmp/"
STORE_BASE = "/var/www/html/%s_store_base.html"
LEGACY_BASE = "/var/www/%s.html" # FIXME : the URLs of the legacy stores.

def main():
  # Pull parameters from URL and POST data
  store_id = params.get().getvalue("storeid") # FIXME : not final

  if int(store_id) in c.STORES:
    store_name = c.STORES[store_id][0]
    bundle_id = c.STORES[store_id][1]
  else:
    raise errors.StoreError()

  # Bring in the HTML template.
  parser = etree.HTMLParser()
  HTMLtree = etree.parse("/var/www/html/"+store_name+"_template.html", parser)
  legacyHTMLtree = etree.parse("/var/www/html/legacy_"+store_name+"_template.html", parser)


  # Create db connection for fetching promotions.
  dB = db_connect.OpenDB()
  
  # Create and make query to retrieve data for the currently stored issues.
  items_query = """
    SELECT *
    FROM content_items
    WHERE bundle_id = '%s'
    ORDER BY publication_date DESC
  """ % (bundle_id)
  items_results = dB.SelectQuery(items_query)
  
  # Create and make query to retrieve preview image urls.
  previews_query = """SELECT content_item_id, image_url FROM previews"""
  previews_results = dB.SelectQuery(previews_query)
  
  # Close db connection.
  dB.Close()


  # Create a workable dictionary of the preview image query.
  previews_dict = datautils.workablepreviews(previews_results)

  # Pop off the first item in the result as the featured item.
  featured_item = datautils.singleissue(items_results.pop(0), previews_dict)
  
  # Get a list of objects from the result, allowing the issue metadata to be 
  # accessed by name rather than index in the query results.
  previous_issues = datautils.listissues(items_results, previews_dict)


  # Find the featured section:
  featured_holder = HTMLtree.find(".//div[@id='featured_issue']")
  legacy_featured_holder = legacyHTMLtree.find(".//div[@id='featured_issue']")
  
  # Find the preview section:
  issue_holder = HTMLtree.find(".//div[@id='issue_float_holder']")
  legacy_issue_holder = legacyHTMLtree.find(".//div[@id='issue_float_holder']")
  
  # Find the lightbox section:
  details_holder = HTMLtree.find(".//div[@id='hide_details']")
  legacy_details_holder = legacyHTMLtree.find(".//div[@id='hide_details']")


  # Build the featured issue section.
  featured_id = str(featured_item.info["id"])

  if featured_item.info["price_tier"] > 0:
    featured_action_string = "Buy $"+str(float(featured_item.info["price_tier"]) - 0.01)
  else:
    featured_action_string = "Download"

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
            CLASS("feature_button","action_button","buy_button")
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
  
  details_holder.append(builders.buildlightbox(featured_item, featured_action_string))
  

  # Build the list of previous issues and the detail panels for each.  
  for issue in previous_issues:
    previous_id = str(issue.info["id"])

    if issue.info["price_tier"] > 0:
      issue_action_string = "Buy $"+str(float(issue.info["price_tier"]) - 0.01)
    else:
      issue_action_string = "Download"
  
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
              CLASS("left_button","action_button","buy_button")
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
    
    details_holder.append(builders.buildlightbox(issue, issue_action_string))

  legacy_featured_holder = featured_holder
  legacy_issue_holder = issue_holder
  legacy_details_holder = details_holder


  # Write the generated HTML to a temporary file. Using temporary files prevents race conditions.
  data = etree.tostring(HTMLtree)
  tmp = tempfile.mkstemp(dir=TEMP_BASE)
  legacy_tmp = tempfile.mkstemp(dir=TEMP_BASE)

  bytes_written = os.write(tmp[0], data)
  os.write(legacy_tmp[0], data)
  os.close(tmp[0])
  os.close(legacy_tmp[0])

  # Move the temporary file to the final URL.
  # FIXME : do we need to fix permissions here?
  os.rename(tmp[1], STORE_BASE % (store_name))
  os.rename(legacy_tmp[1], LEGACY_BASE % (store_name))

  return bytes_written