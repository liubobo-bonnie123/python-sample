class Issue(object):
  """This class is used as a C-style struct for passing around information about issues. Said
  information is stored in a dictionary for easy iteration if need be."""
  def __init__(self):
    self.info = {
      "id" : None,
      "bundle_id" : None,
      "description" : None,
      "price_tier" : None,
      "download_url" : None,
      "thumbnail_url" : None,
      "cover_url" : None,
      "in_app_purchase_id" : None,
      "publication_date" : None,
      "edition" : None,
      "title" : None,
      "subtitle" : None,
      "item_addition_datetime" : None,
      "preview_urls" : None
    }