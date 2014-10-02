import re

f=open("/Users/poorvadixit/Downloads/10001.txt", "r")
tagData=f.read()

title=re.findall(r"Title.*\n",tagData)[0].split(':')[1].strip()

author=re.findall(r"Author.*\n",tagData)[0].split(':')[1].strip()

language=re.findall(r"Language.*\n",tagData)[0].split(':')[1].strip()

all=[title,author,language]

allvar= "   ".join(all)

f1=open("/Users/poorvadixit/Desktop/BOLIU/result.txt", "w")
f1.write(allvar)
f1.close()
