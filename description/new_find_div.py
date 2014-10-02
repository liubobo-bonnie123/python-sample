
from lxml import etree
from lxml.html.builder import *

import tempfile
import os
import db_connect
import builders
import datautils
import params
import errors
import config as c
import sys
import pdb

from textutils import makeunicode, makecleanelement, trimtext
from efactory import CLASS, SRC, HREF, ID
from BeautifulSoup import UnicodeDammit
from textutils import makeunicode, makecleanelement, trimtext

# FIXME : for development/testing only
import cgi, cgitb
cgitb.enable()

def main(file_fullname):
    tmp_list = []
    parser = etree.HTMLParser()
    HTMLtree = etree.parse(file_fullname, parser)
    # print 'HTMLtree' + type(HTMLtree)
    description_holder = HTMLtree.findall(".//div")
    for items in description_holder:
        tmp = items.xpath("string()")
        tmp = tmp.strip('\n').replace('\n',' ')
        tmp_list.append(tmp)
        # print tmp
    des = ' '.join(tmp_list)
    des = des.strip('\n').replace('\n',' ')
    if type(des) != unicode:
        des = unicode(des, 'utf-8')
    print des
    print type(des)
    # print 'description_holder' + type(description_holder[0])
    # print description_holder
    # print description_holder
    # print etree.tostring(description_holder)
    # print type(description_holder)
    # x=description_holder.findtext(".//p")
    # print x
    # data = etree.tostring(description_holder)
    # print data
    # print description_holder
    # data=[]
    # JOIN=''
    # EMPTY=''
    # for items in description_holder:
    #     print type(items)
    #     fake_des_patten_set = ('www', 'gutenberg', 'COPYRIGHTED', 'Project', 'eBook', 'EBook')
    #     tmp = items.xpath("string()")
    #     # print tmp
    #     # tmp_str = str(tmp)
    #     # # pdb.set_trace()
    #     # print 'tmp' 
    #     # print type(tmp)
    #     # print 'tmp_str' 
    #     # print type(tmp_str)
    #     # tmp_str = str(tmp)
    #     # print type(tmp_str)
    #     FAKE=''
    #     COUNT=0
    #     for patten in fake_des_patten_set:
    #         # pdb.set_trace()
    #         if tmp.find(patten) != -1:
    #             FAKE = 'yes'
    #             # pdb.set_trace()
    #             break
    #         else:
    #             COUNT=COUNT+1
    #             # pdb.set_trace()
    #             continue
    #     if COUNT == 6:
    #         FAKE == 'no'
    #     # tmp_str = etree.tostring(tmp)
    #     # print type(tmp_str)
    #     if FAKE == 'yes':
    #         continue#continue from items
    #     else:
    #         tmp_list = tmp.strip('/n').split(' ')
    #         len_list = len(tmp_list)
    #         if JOIN == 'join':
    #             # tmp.replace('u\'\u201c', '&#8220')
    #             # tmp.replace('u\'\u201d', '&#8221')
    #             # tmp.encode('utf-8')
    #             # tmp_final = tmp.replace('\n',' ')
    #             # print str(tmp_final)
    #             tmp_des = [des,tmp.replace('\n',' ')]
    #             des = ' '.join(tmp_des)
    #             EMPTY='no_empty'
    #             break
    #         else:
    #             if len_list > 5:
    #                 if len_list < 50:
    #                     # u'\u201c'.encode('utf-8')
    #                     # tmp.replace('u\'\u201c\'', '&#8220')
    #                     # tmp.replace('u\'\u201d', '&#8221')
    #                     # des = tmp.encode('utf-8')
    #                     # tmp_final = tmp.replace('\n',' ')
    #                     # print str(tmp_final)
    #                     des = tmp.replace('\n',' ')
    #                     JOIN = 'join'
    #                     continue
    #                 else:
    #                     # tmp.replace('u\'\u201c', '&#8220')
    #                     #  tmp.replace('u\'\u201d', '&#8221')
    #                     # des = tmp.encode('utf-8')
    #                     fake_str=''
    #                     # des = tmp
    #                     # tmp_final = tmp.replace('\n',' ')
    #                     # print str(tmp_final)
    #                     tmp_des = [fake_str,tmp.replace('\n',' ')]
    #                     des = ' '.join(tmp_des)
    #                     EMPTY='no_empty'
    #                     break
    #             else:
    #                 continue       
    # if EMPTY=='':
    #     des = 'no_des'
    #     # des = unicode('no_des', 'utf-8')
    #     
    # if type(des) != unicode:
    #     des = unicode(des, 'utf-8')
    # print des
    # print type(des)
    # # f2=open(sys.argv[2], "a")
    # # f2.write(des)
    # # f2.write('\n')
if __name__ == "__main__":
    main(sys.argv[1])


    
