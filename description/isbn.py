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

for info in tagData:
    isbn=info.split('\t')[0].split('_')[1]
    # pdb.set_trace()
    new_info = info.replace(info.split('\t')[0],isbn)
    f2=open(sys.argv[2], "a")
    f2.write(new_info)

    
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
