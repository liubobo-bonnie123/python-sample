#!/usr/bin/python2.6

from lxml import etree

import json
import params
import errors
import config as c

# FIXME : for development/testing only
import cgi, cgitb
cgitb.enable()

def main():
  # Pull parameters from URL and POST data
  post_json = json.JSONDecoder().decode(params.get().getvalue("data")) # FIXME : not final
  store_id = params.get().getvalue("storeid") # FIXME : not final

  if int(store_id) in c.STORES:
    store_name = c.STORES[store_id][0]
  else:
    raise errors.StoreError()

  # Bring in the HTML template.
  parser = etree.HTMLParser()
  HTMLtree = etree.parse("/var/www/html/"+store_name+"_store_base.html", parser)


  # Create a list of strings representing content_item_ids that are entitled.
  entitled = []
  for entitled_id in post_json["entitled"]: # FIXME : not final
    entitled.append(str(entitled_id))

  # Create a list of strings representing content_item_ids that are installed.
  installed = []
  for installed_id in post_json["installed"]: # FIXME : not final
    installed.append(str(installed_id))


  # Change all the buttons on the page to their correct state:
  for entitled_item in entitled:
    if entitled_item in installed:
      continue
    else:
      ent_links = HTMLtree.findall(".//a[@class='item"+entitled_item+"']")
      for ent_link in ent_links:
        ent_button = ent_link.find("div")
        ent_button.text = "Download"
        ent_button.set("class", ent_button.get("class")+" purchased_button")
  
  for installed_item in installed:
    inst_links = HTMLtree.findall(".//a[@class='item"+installed_item+"']")
    for inst_link in inst_links:
      inst_button = inst_link.find("div")
      inst_button.text = "Read"
      inst_button.set("class", inst_button.get("class")+" downloaded_button")
  
  print "Content-type: text/html\n"
  print etree.tostring(HTMLtree)

if __name__ == "__main__":
  main()