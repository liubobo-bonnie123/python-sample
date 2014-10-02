import os
import os.path
import re
import pdb

# dirname="/Volumes/storage/clients/francisco/deliveries/iOS/RH/converted"
# 
# bookdir=os.listdir(dirname)
# 
# filename=open("/Volumes/storage/clients/for-side/BUILDCODE/ForSide/list/RH.txt", "r")
# 
# tagData=filename.read()
# 
# tag=tagData.split('\n')

f=open('/Users/poorvadixit/Desktop/BOLIU/list.txt','r')
ff=open('/Users/poorvadixit/Desktop/BOLIU/long_title.txt','r')
fff=open('/Users/poorvadixit/Downloads/list.txt','r')
# 
# li=[]

t=f.read()
tt=ff.read()
ttt=fff.read()

tagData=t.split('\n')
tagDataa=tt.split(' \n')



tagDataaa=ttt.split('\n')

for elem in tagDataa:
  
    if elem in tagData:
        elem_index=tagData.index(elem)
        target=tagDataaa[elem_index]
        f2=open("/Users/poorvadixit/Desktop/BOLIU/longtitle_book_info.txt", "a")
          
        f2.write(target)
        f2.write('\n')
        print elem
    else:
        
        f2=open("/Users/poorvadixit/Desktop/BOLIU/missing_title.txt", "a")
          
        f2.write(elem)
        f2.write('\n')
