#!/usr/bin/python2.6

from lxml import etree
from lxml.html.builder import *

from textutils import makeunicode, makecleanelement
from efactory import CLASS, SRC, HREF, ID

def buildlightbox(issue, issue_action_string):
  """ makelightbox : Issue -> ElementTree Object 
  Takes an instance of class Issue and returns a complete lightbox element that can then
  be appended to the page.
  """
  
  issue_id = str(issue.info["id"])

  # Create the popup lightbox.
  issue_details = etree.Element("div")
  issue_details.set("class","issue_details")
  issue_details.set("id","frame"+issue_id)
  
  # Append the close button in the upper right.
  issue_details.append(DIV(DIV(makeunicode("&nbsp;"), CLASS("close_button")),CLASS("close_holder")))
  
  issue_description = ""
  if issue.info["description"] is not None:
    issue_description = makecleanelement("<p>",issue.info["description"],"</p>")
  
  # Append the details section.
  issue_details.append(
    DIV(
      DIV(
        IMG(SRC(issue.info["thumbnail_url"])),
        A(
          DIV(
            issue_action_string,
            CLASS("issue_button","action_button","buy_button")
          ),
          HREF("sm://itemOpen/"+issue_id),
          CLASS("item"+issue_id)
        ),
        CLASS("issue_images")
      ),
      DIV(
        H2(makeunicode(issue.info["title"])),
        issue_description,
        CLASS("issue_desc")
      ),
      CLASS("issue_float_holder")  
    )
  )

  # Append the preview images.
  preview_images = etree.Element("div")
  preview_images.set("class","preview_holder")
  
  for preview_url in issue.info["preview_urls"]:
    etree.SubElement(preview_images, "img").set("src", preview_url)
  
  issue_details.append(
    DIV(
      DIV(
        preview_images,
        CLASS("scrollable_previous")
      ),
      CLASS("wrapper_previous")
    )
  )
  
  return issue_details