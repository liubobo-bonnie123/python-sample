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



f=open(sys.argv[1],'r')
info_list=f.readlines()
COUNT = 0
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
                        print file_fullname
                        img_src=file_fullname                                                            
                        img_dst='/Users/poorvadixit/Desktop/forside/'+title+'.html'
                        shutil.copy(img_src,img_dst)
                        COUNT += 1
                        DONE='done'
                        break
                    if DONE=='done':
                        break#if pattern break from pattern
                if DONE=='done':
                    break#for pattern from element
        if DONE=='done':
            break#for element break from root



print COUNT                    
            

