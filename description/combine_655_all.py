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
    if items.strip('\n').split('\t')[1] != 'no_des':
        pass
    else:
        print items
        for six in tagDataa:
            if six.strip('\n').split('\t')[0] == items.strip('\n').split('\t')[0]:
                if six.strip('\n').split('\t')[1] != '':
                    # pdb.set_trace()
                    new_des = six.strip('\n').split('\t')[1]
                    tmp_items = [items.strip('\n').split('\t')[0],new_des]
                    tmp_items1 = '\t'.join(tmp_items)
                    tmp_items2 = [tmp_items1,'\n']
                    items = ' '.join(tmp_items2)
                    print items
                    break
                else:
                    break
            else:
                continue
    f2=open(sys.argv[3], "a")
    f2.write(items)
    
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
