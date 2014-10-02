import classes

def workablepreviews(previews_results):
  """ workablepreviews : tuple -> dict 
  Takes a result from a query to the previews table and builds a workable dictionary of the
  results. Returned dictionary has keys of content_item_id and values of lists of urls.
  """
  previews = {}

  for image in previews_results:
    if image[0] in previews:
      previews[image[0]].append(image[1])
    else:
      previews[image[0]] = [image[1]]

  return previews

def singleissue(issue_tuple, preview_dict):
  """ singleissue : tuple -> Issue object 
  Takes a single result tuple from a selection query and returns an Issue object reflecting the
  passed result.
  """
  issue = classes.Issue()
  issue.info["id"] = issue_tuple[0]
  issue.info["bundle_id"] = issue_tuple[1]
  issue.info["description"] = issue_tuple[2]
  issue.info["price_tier"] = issue_tuple[3]
  issue.info["download_url"] = issue_tuple[4]
  issue.info["thumbnail_url"] = issue_tuple[5]
  issue.info["in_app_purchase_id"] = issue_tuple[6]
  issue.info["publication_date"] = issue_tuple[7]
  issue.info["edition"] = issue_tuple[8]
  issue.info["title"] = issue_tuple[9]
  issue.info["subtitle"] = issue_tuple[10]
  issue.info["item_addition_datetime"] = issue_tuple[11]
  issue.info["cover_url"] = issue_tuple[12]

  issue.info["preview_urls"] = []
  if issue.info["id"] in preview_dict:
    for url in preview_dict[issue.info["id"]]:
      issue.info["preview_urls"].append(url)

  return issue
  
def listissues(issue_list, preview_dict):
  """ singleissue : list -> list
  Takes a list of result tuples from a selection query and returns a list of Issue objects
  relecting the passed results.
  """
  issue_objects = []
  
  for issue in issue_list:
    issue_objects.append(singleissue(issue, preview_dict))
  
  return issue_objects