# Each store in this dictionary should have the following values defined:
#  - Bundle ID
#  - Template name. This will tell the page generator which HTML template to use.
#    For example, a template name of "esquire" will point the page generator
#    to the template with URL "/var/www/html/esquire_template.html".
#  - Store name. This will determine the filename of the generated HTML. For 
#    example, a store name of "oprah-test" will result in a static store with
#    URL "/var/www/hearst-store/oprah-test/index.html".

STORES = {
  0 : ("com.hearst.opr.shell", "oprah", "oprah"),
  1 : ("com.hearst.esq.shell", "esquire", "esquire"),
  2 : ("com.scrollmotion.oprah-shell-test", "oprah", "oprah-test"),
  3 : ("com.scrollmotion.esquire-shell-test", "esquire", "esquire-test")
}