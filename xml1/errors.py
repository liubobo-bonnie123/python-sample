class StoreError(Exception):
  """Custom exception raised when an incorrect store name/ID is 
  passed to the page generation script."""

  def __init__(self):
    self.msg = "Store ID Error: store ID parameter passed to store generation is invalid."
    
  def __str__(self):
    return repr(self.msg)