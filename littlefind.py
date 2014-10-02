import os
import os.path
import re
import pdb
import string

f_bisac=open('/Users/poorvadixit/Desktop/BOLIU/map_reverse_list.txt','r')
ff_bisac=open('/Users/poorvadixit/Desktop/BOLIU/titleall.txt','r')
i=0
tag_bisac=f_bisac.read()
tagData_bisac=tag_bisac.split('\n')

tag_bisacc=ff_bisac.read()
tagData_bisacc=tag_bisacc.split('\n')

for elem in tagData_bisacc:
    if elem in tagData_bisac:
        pass
    else:
        print elem
        i=i+1
print i