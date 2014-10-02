import os
import os.path
import re
import pdb
import string

f_bisac=open('/Users/poorvadixit/Desktop/BOLIU/map_reverse_list.txt','r')
nf_bisac=open('/Users/poorvadixit/Desktop/BOLIU/title_bisac_new.txt','r')

tag_bisac=f_bisac.read()
tagData_bisac=tag_bisac.split('\n')


ntag_bisac=nf_bisac.read()
ntagData_bisac=ntag_bisac.split('\n')

for elem in tagData_bisac:  
    if elem not in ntagData_bisac:
        print elem
        f2=open("/Users/poorvadixit/Desktop/BOLIU/missing_map_mapreverse.txt", "a")

        f2.write(elem)
        f2.write('\n')
    else:
        pass
    