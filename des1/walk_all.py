"""
move.py

for general

Created by Bo Liu on 2011-03-28.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import os
import os.path
import re
import pdb
import string
import glob
import sys
import shutil



def find_pclass_element(tagData):
    pclass_list=re.findall('<p class=',tagData)
    pclass_number=len(pclass_list)
    # print pclass_number
    # pdb.set_trace()
    count=0
    for i in range(pclass_number):
        head=string.find(tagData,'<p class=')
        tag_tem=tagData[head:]
        end_tem=string.find(tag_tem,'</p>')
        tag_final=tag_tem[:end_tem][16:].strip('</p>')
        count=count+1
        # pdb.set_trace()
        if re.findall("<",tag_final)!=[]:
            tagData=tag_tem[end_tem:]
        elif re.findall(">",tag_final)!=[]:
            tagData=tag_tem[end_tem:]
        else:
            tag_tem_word=tag_final.split(' ')
            # print tag_tem_word
            if len(tag_tem_word) > 45:
                tag_tem_word_final=tag_tem_word[:44]
                book_des=' '.join(tag_tem_word_final)
                break
            else:
                tagData=tag_tem[end_tem:]
            
    # pdb.set_trace()
    if count==pclass_number:
        book_des='no_description'
            
    return book_des
    
    
def find_pid_element(tagData):
    pid_list=re.findall('<p id=',tagData)
    pid_number=len(pid_list)
    if pid_number==0:
        book_des='no_pid'
    # print pid_number
    # pdb.set_trace()
    count=0
    for i in range(pid_number):
        head=string.find(tagData,'<p id=')
        tag_tem=tagData[head:]
        end_tem=string.find(tag_tem,'</p>')
        tag_final=tag_tem[:end_tem][16:].strip('</p>')
        count=count+1
        # pdb.set_trace()
        if re.findall("<",tag_final)!=[]:
            tagData=tag_tem[end_tem:]
        elif re.findall(">",tag_final)!=[]:
            tagData=tag_tem[end_tem:]
        else:
            tag_tem_word_one=tag_final.split('\n')
            tag_tem_word_two=' '.join(tag_tem_word_one)
            tag_tem_word=tag_tem_word_two.split(' ')
            # print tag_tem_word
            if len(tag_tem_word) > 50:
                tag_tem_word_final=tag_tem_word[:49]
                book_des=' '.join(tag_tem_word_final)
                break
            else:
                tagData=tag_tem[end_tem:]

    # pdb.set_trace()
    # print count
    if count==pid_number:
        book_des='no_description'

    return book_des

def find_p_element(tagData):
    p_result_findall=re.findall("<p>.*.</p>", tagData)
    if p_result_findall!=[ ]:
        book_des='no_description'
    else:
        p_number=len(p_result_findall)
        count=0
        if p_number==0:
            book_des='no_description'
        for element in p_result_findall:
            element_tem=element.strip("<p>").strip(".</p>")
            count=count+1
            if re.findall("<",element_tem)!=[]:
                pass
            elif re.findall(">",element_tem)!=[]:
                pass
            else:
                element_tem_word=element_tem.split(' ');
                if len(element_tem_word)>85:
                    element_tem_word_final=element_tem_word[:49]
                    book_des=' '.join(element_tem_word_final)
                    break
                else:
                    pass
        if count==p_number:
            book_des='no_description'
    # print count
    return book_des
    
def find_n(tagData):
    list_elem=tagData.split('\n')
    n_number=len(list_elem)
    count=0
    
    for elem in list_elem:
        # pdb.set_trace()
        count=count+1
        list_elem_tem=elem.split(' ')
        len_list_elem_tem=len(list_elem_tem)
        if len_list_elem_tem>50:
            elem_final=elem.strip('<p').strip('</p>')
            book_des=elem_final
            break
    if count==n_number:
        book_des='no_description'
    
    return book_des



if __name__ == '__main__':
    f=open(sys.argv[1],'r')
    info_list=f.readlines()
    COUNT = 1
    for elem in info_list:
        DONE=''
        title=elem.strip()
        title_path='/Volumes/storage/books/Public_Domain/unzipped_epubs_to_move/_ready/'+title+'/Assets/Epub/OEBPS/'
        # pdb.set_trace()
        patten_set = ('-0.html', '-0.htm.html', '-0.txt.html', '-0.htm', '-0.htm.htm', '-0.txt.htm','0.html')
        for root, dirs, files in os.walk(title_path):
            # for sub_dir in dirs:
            #     if 'images' in sub_dir.lower():
            #         image_path = os.path.join(root, sub_dir)
            for element in files:
                # if os.path.splitext(element)[1] == '.jpg':
                fake_file=re.findall('^._', element)
                if fake_file==[]:
                    for patten in patten_set:
                        if patten in element:
                            file_fullname=os.path.join(root, element)
                            # pdb.set_trace()
                            f_html=open(file_fullname, "r")
                            tagData=f_html.read()
                            # pdb.set_trace()
                            book_des1=find_p_element(tagData)
                            if book_des1=='no_description':
                                book_des2=find_pid_element(tagData)
                                if book_des2=='no_description':
                                    book_des3=find_pclass_element(tagData)
                                    if book_des3=='no_description':
                                        book_des4=find_n(tagData)
                                        f2=open(sys.argv[2], "a")
                                        f2.write(title)
                                        f2.write('\t')
                                        f2.write(book_des4)
                                        f2.write('\n')
                                        DONE='done'
                                        COUNT += 1
                                        print title
                                        break
                                    else:
                                    
                                        f2=open(sys.argv[2], "a")
                                        f2.write(title)
                                        f2.write('\t')
                                        f2.write(book_des3)
                                        f2.write('\n')
                                        DONE='done'
                                        COUNT += 1
                                        print title
                                        break#if pattern break from pattern
                                else:
                                    f2=open(sys.argv[2], "a")
                                    f2.write(title)
                                    f2.write('\t')
                                    f2.write(book_des2)
                                    f2.write('\n')
                                    DONE='done'
                                    COUNT += 1
                                    print title
                                    break#if pattern break from pattern
                            else:
                                f2=open(sys.argv[2], "a")
                                f2.write(title)
                                f2.write('\t')
                                f2.write(book_des1)
                                f2.write('\n')
                                DONE='done'
                                COUNT += 1
                                print title
                                break#if pattern break from pattern
                        if DONE=='done':
                            break#if pattern break from pattern
                    if DONE=='done':
                        break#for pattern from element
            if DONE=='done':
                break#for element break from root



    print COUNT                    
            

