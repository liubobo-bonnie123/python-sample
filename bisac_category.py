import os
import os.path
import re
import pdb


f=open('/Users/poorvadixit/Desktop/BOLIU/bisac_cate_map.txt','r')
ff=open('/Users/poorvadixit/Desktop/BOLIU/mycategory.txt','r')
fff=open('/Users/poorvadixit/Desktop/BOLIU/offical_category.txt','r')
li=[]

t=f.read()
tt=ff.read()
ttt=fff.read()

tagData=t.split('\n')
tagDataa=tt.split('\n')
tagDataaa=ttt.split('\n')

for elem in tagDataa:
    if elem in tagDataaa:
        elem_index=tagDataaa.index(elem)
        bisac=tagData[elem_index].split('\t')[0]
        f3=open("/Users/poorvadixit/Desktop/BOLIU/exact.txt", "a")
        f3.write(elem)
        f3.write(' ')
        f3.write(bisac)
        f3.write('\n')
        
    else:
        print elem