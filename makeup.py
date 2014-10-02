import os
import os.path
import re
import pdb

f=open("/Users/poorvadixit/Desktop/BOLIU/ProjectGTFS.txt","r")
book_GTFS=f.read()
bookGTFS=book_GTFS + '\n'

dirname="/Volumes/PGDVD_2010_04_RC2/ETEXT/"

bookdir=os.listdir(dirname)
for f in bookdir:
    if re.findall("Title</th>\n<td>.*</td>", tagData)==[ ]:
         title='no_title'
    else:
      
         title=re.findall("Title</th>\n<td>.*</td>", tagData)[0].split('</th>\n<td>')[1].strip('</td>')
         result=re.findall(title + ".*\t.*\t.*\t.*\n",bookGTFS)
         if result=[ ]:
            pass
         else:
            bisac=result[0].split('\t')[2]
            

