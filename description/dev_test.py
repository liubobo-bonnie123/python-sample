import sys
import os
import pdb
import simpledb
import os.path
import re
import string
from lxml import etree
from lxml.html.builder import *


# FIXME : for development/testing only
import cgi, cgitb
cgitb.enable()

def new_find(file_fullname):
    parser = etree.HTMLParser()
    HTMLtree = etree.parse(file_fullname, parser)
    description_holder = HTMLtree.findall(".//p")
    JOIN=''
    EMPTY=''
    for items in description_holder:
        # print type(items)
        fake_des_patten_set = ['www.gutenberg.net', 'COPYRIGHTED', 'Project', 'eBook']
        tmp = items.xpath("string()")
        FAKE=''
        COUNT=0
        for patten in fake_des_patten_set:
            if tmp.find(patten) != -1:
                FAKE = 'yes'
                break
            else:
                COUNT=COUNT+1
                continue
        if COUNT == 4:
            FAKE == 'no'
        if FAKE == 'yes':
            continue#continue from items
        else:
            tmp_list = tmp.strip('/n').split(' ')
            len_list = len(tmp_list)
            if JOIN == 'join':
                tmp_des = [des,tmp.replace('\n',' ')]
                des = ' '.join(tmp_des)
                EMPTY='no_empty'
                break
            else:
                if len_list > 20:
                    if len_list < 50:
                        des = tmp.replace('\n',' ')
                        JOIN = 'join'
                        continue
                    else:
                        fake_str=''
                        tmp_des = [fake_str,tmp.replace('\n',' ')]
                        des = ' '.join(tmp_des)
                        EMPTY='no_empty'
                        break
                else:
                    continue       
    if EMPTY=='':
        des = 'no_des'
    # if type(des) != unicode:
    #     des = unicode(des, 'utf-8')
    # print des
    # print type(des)
    return des


if __name__ == '__main__':
    f=open(sys.argv[1],'r')
    info_list=f.readlines()
    COUNT = 1
    dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
    # pdb.set_trace()
    for elem in info_list:
        DONE=''
        title=elem.strip()
        title_path='/storage/books/Public_Domain/unzipped_epubs_to_move/_ready/'+title+'/Assets/Epub/OEBPS/'
        # pdb.set_trace()
        patten_set = ('-0.html', '-0.htm.html', '-0.txt.html', '-0.htm', '-0.htm.htm', '-0.txt.htm','0.html')
        for root, dirs, files in os.walk(title_path):
            # for sub_dir in dirs:
            #     if 'images' in sub_dir.lower():
            #         image_path = os.path.join(root, sub_dir)
            for element in files:
                # pdb.set_trace()
                # if os.path.splitext(element)[1] == '.jpg':
                fake_file=re.findall('^._', element)
                if fake_file==[]:
                    www_file=re.findall('^www', element)
                    if www_file!=[]:
                        for patten in patten_set:
                            if patten in element:
                                file_fullname=os.path.join(root, element)
                                # pdb.set_trace()
                                description=new_find(file_fullname)
                                # pdb.set_trace()
                                print description
                                print type(description)
                                try:
                                    # description=info.split('\t')[1].strip('\n').decode('utf_8').replace('\'', '')
                                    description.decode('utf_8').replace('\'', '&#8217').replace('\"', '&#8220').replace('\"', '&#8221')
                                    # isbn=info.split('\t')[0].split('_')[1]
                                    qry = '''INSERT INTO description(title, des) VALUES (\'%s\',\'%s\')''' % (title, description)
                                    try:
                                        dbconn.ChangeQuery(qry)
                                        dbconn.Commit()
                                        print title, 'is done'
                                    except:
                                        print title, 'is bad'
                                    
                                except:
                                    log = open('./bad_textcode.txt', 'a')
                                    log.write(title)
                                    log.close()
                                DONE='done'
                                COUNT += 1
                                # print title
                                break#if pattern break from pattern
                            if DONE=='done':
                                break#if pattern break from pattern
                        if DONE=='done':
                            break#for pattern from www_file
                    if DONE=='done':
                        break#for pattern from fake_file
            if DONE=='done':
                break#for element break from root
    dbconn.Commit()
    print COUNT                    
    
# if __name__ == '__main__':
#     info_list = open(sys.argv[1]).readlines()
#     dbconn = simpledb.SimpledbClass("pgsql", "localhost", "dev", "", "dev")
#     for info in info_list:
#         insert_des(info, dbconn)
# 
#     dbconn.Commit()
