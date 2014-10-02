import os
import os.path
import re
import pdb


f=open('/Users/poorvadixit/Desktop/BOLIU/map_list.txt','r')
ff=open('/Users/poorvadixit/Desktop/BOLIU/map_reverse_list.txt','r')
# fff=open('/Users/poorvadixit/Desktop/BOLIU/title_bisac_map.txt','r')

li=[]

t=f.read()
tt=ff.read()
# ttt=fff.read()

tagData=t.split('\n')
tagDataa=tt.split('\n')
# tagDataaa=ttt.split('\n')

for elem in tagDataa:
    if elem in tagData:
        # elem_index=tagDataa.index(elem)
        #         bisac=tagDataaa[elem_index].split('\t')[1]
        #         f3=open("/Users/poorvadixit/Desktop/BOLIU/map.txt", "a")
        #         f3.write(elem)
        #         f3.write('\n')
        #         f3.write(bisac)
        #         f3.write('\n')
        li.append(elem)
        # print elem
    else:
        pass
        # print elem
# print tagData
# lilen=len(tagData)
# 
# 
# print tagDataa
# lilena=len(tagDataa)
# print lilena
# print lilen
for elem in tagDataa:
    elem_count=tagDataa.count(elem)
    if elem_count > 1:
        # print elem
        tagDataa.remove
print '\n'*4

for elem in tagData:
    elem_count_s=tagData.count(elem)
    if elem_count_s > 1:
        print elem
        
        

               #  
               # f2=open("/Users/poorvadixit/Desktop/BOLIU/missing_book.txt", "a")
               # 
               # f2.write(elem)
               # f2.write('\n')
               # print elem
               # 
               
# for elem in tagData:
#     if elem in tagDataa:
#         
#         elem_index_rev=tagDataa.index(elem)
#         bisac=tagDataaa[elem_index_rev].split('\t')[1]
#         f3=open("/Users/poorvadixit/Desktop/BOLIU/map_reverse.txt", "a")
#         f3.write(elem)
#         f3.write('\n')
#         f3.write(bisac)
#         f3.write('\n')
#         print elem
#     else:
#         pass
