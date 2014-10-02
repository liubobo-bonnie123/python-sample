import os
import os.path
import re
import pdb
import string



li_titleinbisac=[]
li_titlenotin=[]

# f_bisac=open('/Users/poorvadixit/Desktop/BOLIU/map.txt','r')
# nf_bisac=open('/Users/poorvadixit/Desktop/BOLIU/map_list.txt','r')
f_bisac=open('/Users/poorvadixit/Desktop/BOLIU/allbisac_map.txt','r')
nf_bisac=open('/Users/poorvadixit/Desktop/BOLIU/allbisac_title.txt','r')

tag_bisac=f_bisac.read()
tagData_bisac=tag_bisac.split('\n')


ntag_bisac=nf_bisac.read()
ntagData_bisac=ntag_bisac.split('\n')
# 
# nntag_bisac=nnf_bisac.read()
# nntagData_bisac=nntag_bisac.split('\n')

#booklist in the excel file ProjectGTFS
f=open("/Users/poorvadixit/Desktop/BOLIU/ProjectGTFS.txt","r")
book_GTFS=f.read()
bookGTFS=book_GTFS + '\n'


#"/Volumes/PGDVD_2010_04_RC2/ETEXT/"
dirname="/Volumes/PGDVD_2010_04_RC2/ETEXT/"
#"/Users/poorvadixit/Desktop/test/"
#"/Volumes/PGDVD_2010_04_RC2/ETEXT/"
#"
#pdb.set_trace()
bookdir=os.listdir(dirname)
#pdb.set_trace()
for f in bookdir:
  #
  
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
          #author
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
            
             
          #title
             # if re.findall("Title</th>\n<td>.*\n?.*\n?.*\n?.*</td>\n</tr>\n<tr>\n<th scope="row">Language", tagData)==[ ]:
             #                  title='no_title'
             #                  bisac='no_bisac'
             #              else:          
             #                  title = re.findall("Title</th>\n<td>.*\n?.*\n?.*\n?.*</td>", tagData)[0].split('</th>\n<td>')[1].strip('</td>')
             #                  if title == 'The Real America in Romance, Volume 6; a Century Too Soon (A Story':
             #                     title_tem = 'The Real America in Romance, Volume 6; a Century Too Soon'
             #                  elif title=='Gems (?) of German Though':
             #                     title_tem='Gems'
             #                  else:
             #                     title_tem=title
            if re.findall('Title',tagData)==[ ]:
                title='no_title'
                
            else:
                head=string.find(tagData,'>Title</th>')
                end=string.find(tagData,'>Language</th>')
                target=tagData[head:end]
                title_tem=target.split('</th>\n<td>')[1].split('</td>\n</tr>\n<tr>\n')[0].split('\n')
                title=' '.join(title_tem)
                    
             
                           
                         # print titlecd
                # bisac
                if title in ntagData_bisac:
                    elem_index=ntagData_bisac.index(title)
                                               
                                               
                    bisac=tagData_bisac[elem_index].split('\t')[1]
                
                
                    # li_titleinbisac.append(title)
                    #                     f3=open("/Users/poorvadixit/Desktop/BOLIU/title_bisac_new.txt", "a")
                    #                     f3.write(title)
                    #                     f3.write('\n')
                    
                
                else:
                    bisac='no_bisac'
                    li_titlenotin.append(title)
                # try:
                #                     result=re.findall(title + ".*\t.*\t.*\t",bookGTFS)
                #                     bisac=result[0].split('\t')[2]
                #                                                   
                #                 # if result==[ ]:
                #                     # bisac='no_bisac'
                #                 except:
                #                     bisac='no_bisac'
                    # bisac=result[0].split('\t')[2]
                                                            
          #language
            if re.findall("Language</th>\n<td>.*</td>", tagData)==[ ]:
                language='no_language'
            else:
          
                language=re.findall("Language</th>\n<td>.*</td>", tagData)[0].split('</th>\n<td>')[1].strip('</td>')
          
          #locclass, category, sub_category
            if re.findall("LoC Class</th>\n<td>.*</td>", tagData)==[ ]:
                locclass='no_locclass'
                category='no_category'
                sub_category='no_sub_category'
            else:
          
                locclass=re.findall("LoC Class</th>\n<td>.*</td>", tagData)[0].split('</th>\n<td>')[1].strip('</td>')
                category=locclass.split(':')[1].strip()
                try:
                
                    sub_category=locclass.split(':')[2].strip()
                
                except:
                    print full_filename + 'has no subcategory'
                    sub_category='no_sub_category'
        
          
            book_info_list=[full_filename,author,title,language,locclass,bisac,category,sub_category]
          
            allvar="\t".join(book_info_list)
          
          #print allvar
          
            f2=open("/Users/poorvadixit/Desktop/BOLIU/booklist_new.txt", "a")
          
            f2.write(allvar)
            f2.write('\n')
            print full_filename 
# len1=len(li_titleinbisac)
# len2=len(li_titlenotin)
# print len1
# print len2
# print li_titleinbisac
# print li_titlenotin
            
          
