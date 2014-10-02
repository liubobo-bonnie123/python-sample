"""
has_des.py

Created by Bo Liu on 2011-03-26.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import os
import os.path
import re
import pdb
import string
import sys


f=open(sys.argv[1],'r')
tagData=f.readlines()
ff=open(sys.argv[2],'r')
tagDataa=ff.readlines()
for items in tagData:
    # pdb.set_trace()
    # print items
    print items
    FIND=''
    for six in tagDataa:
        # pdb.set_trace()
        if six.strip('\n').split('\t')[0].strip() == items.strip('\n').split('\t')[0]:
            FIND='find'
            break
        else:
            continue
    if FIND == '':
        f2=open(sys.argv[3], "a")
        f2.write(items)
        print items
    
#                 
#                 
# tag=tagData.split('\n')
# for elem in tag:
#     print elem
#     if elem.split(' ')[0]=='no_des':
#         print elem.split(' ')[1]
#         f2=open(sys.argv[2], "a")
#         f2.write(elem)
#         f2.write('\n')
#     else:
#         pass
