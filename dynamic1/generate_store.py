#!/usr/bin/python2.6

import tempfile, os

from lxml import etree
from lxml.html.builder import *

import db_connect, builders, datautils
from textutils import makeunicode, makecleanelement, trimtext
from efactory import CLASS, SRC, HREF, ID

TEMP_BASE = "/var/www/tmp/"
STORE_BASE = "/var/www/%s_store.html"

# FIXME : for development/testing only
import cgi, cgitb
cgitb.enable()

def main(store_name):
  # Bring in the HTML template.
  parser = etree.HTMLParser()
  HTMLtree = etree.parse("/var/www/html/"+store_name+"_template.html", parser)


  # Create db connection for fetching promotions.
  dB = db_connect.OpenDB()

  if store_name == "oprah":
    bundle_id = "com.hearst.opr.shell" # FIXME
  elif store_name == "esquire":
    bundle_id = "com.hearst.esq.shell" # FIXME
  
  # Create and make query to retrieve data for the currently stored issues.
  items_query = """
    SELECT *
    FROM content_items
    WHERE bundle_id = '%s'
    ORDER BY content_item_id DESC
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
        SRC(featured_item.info["thumbnail_url"])
      ),
      HREF("#frame"+featured_id),
      CLASS("show_lightbox")
    )
  )
  featured_holder.append(
    DIV(
      DIV(
        H1(makeunicode(featured_item.info["title"])),
        makecleanelement("<p>",featured_item.info["subtitle"],"</p>"),
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
  
  details_holder.append(builders.buildlightbox(featured_item))


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
    
    details_holder.append(builders.buildlightbox(issue))


  # Write the generated HTML to a temporary file. Using temporary files prevents race conditions.
  data = etree.tostring(HTMLtree)
  tmp = tempfile.mkstemp(dir=TEMP_BASE)

  bytes_written = os.write(tmp[0], data)
  os.close(tmp[0])

  # Move the temporary file to the final URL.
  # FIXME : permissions here.
  # os.chmod(tmp[1]) 
  os.rename(tmp[1], STORE_BASE % (store_name))

  return bytes_written

if __name__ == "__main__":
  main('oprah')