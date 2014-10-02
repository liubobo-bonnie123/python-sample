import os
import os.path
import re
import pdb

dirname="/Volumes/storage/clients/francisco/deliveries/iOS/RH/converted"

bookdir=os.listdir(dirname)

filename=open("/Volumes/storage/clients/for-side/BUILDCODE/ForSide/list/RH.txt", "r")

tagData=filename.read()

tag=tagData.split('\n')

for f in tag:
  
    if f in bookdir:
        print f
    else:
        print f
        f2=open("/Users/poorvadixit/Desktop/BOLIU/missingbook.txt", "a")
          
        f2.write(f)
        f2.write('\n')
