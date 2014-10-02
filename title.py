import os
import os.path
import re
import pdb


dirname="/Volumes/PGDVD_2010_04_RC2/ETEXT/"
#"/Users/poorvadixit/Desktop/test/"
#"/Volumes/PGDVD_2010_04_RC2/ETEXT/"
#"
#pdb.set_trace()
bookdir=os.listdir(dirname)
#pdb.set_trace()
for f in bookdir:
  #pdb.set_trace()
  if f=='.DS_Store':
   
          pass
  #pdb.set_trace()
  else:
  #pdb.set_trace()
          full_filename=os.path.join(dirname, f)

          #print full_filename
          
          filename=open(full_filename, "r")
          
          tagData=filename.read()
          #pdb.set_trace()
          if re.findall("Author</th>\n<td>.*</td>", tagData)==[ ]:
             author='no_author'
          else: 
          
             author=re.findall("Author</th>\n<td>.*</td>", tagData)[0].split('</th>\n<td>')[1].strip('</td>')
          
          if re.findall("Title</th>\n<td>.*</td>", tagData)==[ ]:
             title='no_title'
          else:
          
             title=re.findall("Title</th>\n<td>.*</td>", tagData)[0].split('</th>\n<td>')[1].strip('</td>')

          if re.findall("Language</th>\n<td>.*</td>", tagData)==[ ]:
             language='no_language'
          else:
          
             language=re.findall("Language</th>\n<td>.*</td>", tagData)[0].split('</th>\n<td>')[1].strip('</td>')

          if re.findall("LoC Class</th>\n<td>.*</td>", tagData)==[ ]:
             locclass='no_locclass'
          else:
          
             locclass=re.findall("LoC Class</th>\n<td>.*</td>", tagData)[0].split('</th>\n<td>')[1].strip('</td>')

          
          
          book_info_list=[full_filename,author,title,language,locclass]
          
          allvar="\t".join(book_info_list)
          
          #print allvar
          
          f2=open("/Users/poorvadixit/Desktop/BOLIU/booklist.txt", "a")
          
          f2.write(allvar)
          f2.write('\n')
          print full_filename 
          
          