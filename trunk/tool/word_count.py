#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from os import walk,remove
from os.path import join

output=open("word.txt",'w')

for root, dirs, files in walk("output"):
    for name in files:
        path=join(root,name)
        input=open(path)
        print path
        word={}
        for line in input:
            line=line.strip().decode("utf-8")
            line.decode("utf-8")
            if line[:3]==u">>>":
                kind=line.split('/',1)[0]
            else:
                if line in word:
                    word[line]+=1
                else:
                    word[line]=1
        for k,v in word.iteritems():
            if v>4:
                output.write(k+"\n")
        input.close()
output.close()