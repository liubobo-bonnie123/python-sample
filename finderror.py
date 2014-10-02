import os
import os.path
import re
import pdb


f=open('/Users/poorvadixit/Desktop/BOLIU/titleall.txt','r')
ff=open('/Users/poorvadixit/Desktop/BOLIU/titlebisac.txt','r')
fff=open('/Users/poorvadixit/Desktop/BOLIU/title_bisac_map.txt','r')

li=[]

t=f.read()
tt=ff.read()
ttt=fff.read()

tagData=t.split('\n')
tagDataa=tt.split('\n')
tagDataaa=ttt.split('\n')

# for elem in tagDataa:
#     if elem in tagData:
#         elem_index=tagDataa.index(elem)
#         bisac=tagDataaa[elem_index].split('\t')[1]
#         f3=open("/Users/poorvadixit/Desktop/BOLIU/map.txt", "a")
#         f3.write(elem)
#         f3.write('\n')
#         f3.write(bisac)
#         f3.write('\n')
#         print elem
#     else:
#         pass
               #  
               # f2=open("/Users/poorvadixit/Desktop/BOLIU/missing_book.txt", "a")
               # 
               # f2.write(elem)
               # f2.write('\n')
               # print elem
               # 
               
for elem in tagData:
    if elem in tagDataa:
        
        elem_index_rev=tagDataa.index(elem)
        bisac=tagDataaa[elem_index_rev].split('\t')[1]
        f3=open("/Users/poorvadixit/Desktop/BOLIU/map_reverse.txt", "a")
        f3.write(elem)
        f3.write('\t')
        f3.write(bisac)
        f3.write('\n')
        print elem
    else:
        pass
