import cgi

_fields = None

def get():
  """ Returns the current contents of cgi.FieldStorage. Protects from reading from
  cgi.FieldStorage more than once, which would return an empty result. """
  global _fields
  if not _fields:
    _fields = cgi.FieldStorage()
  return _fields