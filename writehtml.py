from __future__ import unicode_literals
from writemdict import MDictWriter
import os
import codecs
import json

filelist = os.listdir()
mdxcontent = []

content = []
dictionary = {}
for filename in filelist:
  if(filename.split(".")[-1] not in ["html", "htm"]):
    continue
  entryname = filename.replace(".html", '')#".".join(filename.split(".")[0:-1])
  with codecs.open(filename, "r+", encoding='utf-8') as ent:
    entrycontent = ent.read()
    entry = entryname + "\n" + entrycontent
    entry = entry + "\n</>"
  dictionary[entryname] = entrycontent
  mdxcontent.append(entry)
  print(filename)
with codecs.open("notes.txt", 'w+', encoding='utf-8') as f:
  f.write("\n".join(mdxcontent).replace("\n\n", "\n").replace("\n\n", "\n"))
  
writer = MDictWriter(dictionary, title="Notes", description="My best notes!")
outfile = open("notes.mdx", "wb")
writer.write(outfile)
outfile.close()
