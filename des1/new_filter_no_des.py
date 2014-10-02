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
tagData=f.read()
# pdb
tag=tagData.split('\n')
# pdb.set_trace()
for elem in tag:
    print elem
    # pdb.set_trace()
    if elem.split('\t')[1]=='':
        print elem.split('\t')[0]
        f2=open(sys.argv[2], "a")
        f2.write(elem.split('\t')[0])
        f2.write('\n')
    else:
        pass
