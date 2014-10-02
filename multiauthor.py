import os
import os.path
import re
import pdb
import string



# li_titleinbisac=[]
# li_titlenotin=[]
# 
# f_bisac=open('/Users/poorvadixit/Desktop/BOLIU/map.txt','r')
# nf_bisac=open('/Users/poorvadixit/Desktop/BOLIU/map_list.txt','r')
# nnf_bisac=open('/Users/poorvadixit/Desktop/BOLIU/titlebisac.txt','r')
# 
# tag_bisac=f_bisac.read()
# tagData_bisac=tag_bisac.split('\n')
# 
# 
# ntag_bisac=nf_bisac.read()
# ntagData_bisac=ntag_bisac.split('\n')
# 
# nntag_bisac=nnf_bisac.read()
# nntagData_bisac=nntag_bisac.split('\n')
# 
# #booklist in the excel file ProjectGTFS
# f=open("/Users/poorvadixit/Desktop/BOLIU/ProjectGTFS.txt","r")
# book_GTFS=f.read()
# bookGTFS=book_GTFS + '\n'
# 
# 
# #"/Volumes/PGDVD_2010_04_RC2/ETEXT/"
# dirname="/Volumes/PGDVD_2010_04_RC2/ETEXT/"
# #"/Users/poorvadixit/Desktop/test/"
# #"/Volumes/PGDVD_2010_04_RC2/ETEXT/"
# #"
# #pdb.set_trace()
# bookdir=os.listdir(dirname)
# #pdb.set_trace()
# for f in bookdir:
#   #pdb.set_trace()
#   if f=='.DS_Store':
#    
#           pass
#   #pdb.set_trace()
#   else:
#   #pdb.set_trace()
#             full_filename=os.path.join(dirname, f)
# 
#           #print full_filename
#           
#             filename=open(full_filename, "r")
#           
#             tagData=filename.read()
          #pdb.set_trace()
          #author
f=open('/Users/poorvadixit/Desktop/BOLIU/test.HTML','r')
tagData=f.read()


if re.findall("Author</th>\n<td>.*</td>", tagData)==[ ]:
                author='no_author'
else: 
           
                author_1=re.findall("Author</th>\n<td>.*</td>", tagData)[0].split('</th>\n<td>')[1].strip('</td>')
                try:
                    author_2=re.findall("Author</th>\n<td>.*</td>", tagData)[1].split('</th>\n<td>')[1].strip('</td>')
                    try:
                        author_3=re.findall("Author</th>\n<td>.*</td>", tagData)[2].split('</th>\n<td>')[1].strip('</td>')
                        author_tem=[author_1,author_2,author_3]
                        author="/".join(author_tem)
                    except:
                        author_tem=[author_1,author_2]
                        author="/".join(author_tem)
                except:
                    author=author_1
print author
                
                
                              #   
                              # elif author_2 !=[]:
                              #     if author_3==[]:
                              #         author_tem=[author_1,author_2]
                              #         author="/".join(author_tem)
                              #     else:
                              #         author_tem=[author_1,author_2,author_3]
                              #         author="/".join(author_tem)
                        
                
