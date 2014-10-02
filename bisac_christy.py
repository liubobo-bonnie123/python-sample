import os
import os.path
import re
import pdb



f=open('/Users/poorvadixit/Desktop/BOLIU/christy.txt','r')

li=[]


t=f.read()


tagData=t.split('\n')


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
    if elem.split('\t')[1]=='no_bisac':
                # 
                # elem_index_rev=tagDataa.index(elem)
                # bisac=tagDataaa[elem_index_rev].split('\t')[1]
        
        # li.append[elem]
        pass
    else:
        f3=open("/Users/poorvadixit/Desktop/BOLIU/christy_nobisac.txt", "a")
        f3.write(elem)
        f3.write('\n')
        
        print elem
# lenli=len(li)
# print lenli