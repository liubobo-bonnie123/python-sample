import lxml.html
import re
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup

# Text parsing/cleaning utilities #

def maketoken(ugly_string):
  """ maketoken : string -> string
  Returns an XML-tokenized version of the inputted string. XML tokens do not contain the following:
    - leading or trailing whitespace
    - carriage feeds
    - new lines
    - tabs
    - sequences of more than one space
  """
  assert(type(ugly_string) == str or type(ugly_string) == unicode)
  return re.sub('\s+', ' ', ugly_string).strip()
  
def makeunicode(ugly_string):
  """ makeunicode : string -> unicode
  Returns a unicode version of the inputted string. All HTML entities
  in the origin string will be replaced by their unicode equivalents."""
  assert(type(ugly_string) == str or type(ugly_string) == unicode)
  return unicode(BeautifulStoneSoup(ugly_string, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))

def makeXMLfriendly(ugly_string):
  """ makeXMLfriendly : string -> string
  Returns an XML-friendly ASCII version of the inputted string. All special characters
  are replaced by their XML character references."""
  assert(type(ugly_string) == str or type(ugly_string) == unicode)
  return ugly_string.encode('ascii', 'xmlcharrefreplace')

def makecleanelement(open, ugly_string, close):
  """ makecleanelement : string string string -> ElementTree Object
  Returns an ElementTree Object containing the ugly string in element defined by strings
  open and close."""
  assert(type(ugly_string) == str or type(ugly_string) == unicode)
  description_soup = BeautifulSoup(makeunicode(ugly_string))
  return lxml.html.fromstring(open+str(description_soup)+close)

def trimtext(ugly_string, charnum):
  """ trimtext : string int -> string
  Returns the given string trimmed to charnum number of characters and with an 
  appended ellipsis."""
  assert(type(ugly_string) == str or type(ugly_string) == unicode)
  return (ugly_string[:charnum] + ' ..') if len(ugly_string) > charnum else ugly_string