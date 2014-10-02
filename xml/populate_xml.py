import os
import sys
from optparse import OptionParser
import pdb
import json



def main(bookpath, book, xml_template):
    json_file_path = '%s/Uniberg/%s.json' % (bookpath, book)
    f = open(json_file_path)
    tag = f.read()
    json_data = json.loads(tag)
    insert_part=[]
    list_len = len(json_data[u'item'][u'prices'])
    for items in json_data[u'item'][u'prices']:
        price = items[u'item_price']
        country = items[u'item_region_id']
        if json_data[u'item'][u'prices'].index(items) == list_len-1 :
            info = '''\n\t\t<countryInfo countryCode=\'%s\' appPrice=\'%s\'>\n\t\t\t<supportInfo>\n\t\t\t\t<phone number="^^phoneNumber^^" extension="^^phoneNumberExtension^^" />\n\t\t\t\t<emailAddress>^^emailAddress^^</emailAddress>\n\t\t\t\t<supportWebsite>^^supportWebsite^^</supportWebsite>\n\t\t\t\t<companyWebsite>^^companyWebsite^^</companyWebsite>\n\t\t\t\t<marketingEmail>^^marketingEmail^^</marketingEmail>\n\t\t\t</supportInfo>\n\t\t</countryInfo>\n\t'''%(country, price)
        else:
            info = '''\n\t\t<countryInfo countryCode=\'%s\' appPrice=\'%s\'>\n\t\t\t<supportInfo>\n\t\t\t\t<phone number="^^phoneNumber^^" extension="^^phoneNumberExtension^^" />\n\t\t\t\t<emailAddress>^^emailAddress^^</emailAddress>\n\t\t\t\t<supportWebsite>^^supportWebsite^^</supportWebsite>\n\t\t\t\t<companyWebsite>^^companyWebsite^^</companyWebsite>\n\t\t\t\t<marketingEmail>^^marketingEmail^^</marketingEmail>\n\t\t\t</supportInfo>\n\t\t</countryInfo>'''%(country, price)
        insert_part.append(info)
    new_country_Info = ' '.join(insert_part)
    xml_model = open(xml_template,'r')
    xml_model_data = xml_model.read()
    new_xml_data = xml_model_data.replace('<supportedCountries></supportedCountries>', '<supportedCountries>' + new_country_Info + '</supportedCountries>')
    xml_file = open('/Users/poorvadixit/Desktop/xml/' + book + '.xml','a')
    xml_file.write(new_xml_data)
    xml_file.close()
    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--booklist', action='store', dest='booklist', default=False)
    parser.add_option('--path', action='store', dest='path', default=False)
    options, args = parser.parse_args()
    booklist = open(options.booklist).read().split()
    xml_template = '/Volumes/storage/clients/HP/Dev/CREATE-XML/cleaner_sample_xml.xml'
    # xml_template = '/Users/poorvadixit/Desktop/sample_xml.xml'
    for book in booklist:
        bookpath = os.path.join(options.path, book)
        main(bookpath, book, xml_template)