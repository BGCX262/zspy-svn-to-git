#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from os import walk,remove
from os.path import join
from zcut import hash

prime=461

def load(id):
    word_file=open("word.txt")
    word=set()
    for line in word_file:
        line=line.strip().decode("utf-8")
        if hash(line[:2].encode('utf-8'),prime)==id:
            word.add(line)
    word_file.close()
    return word
output=open("kind_count.txt",'w')
for root, dirs, files in walk("output"):
    for name in files:
        path=join(root,name)
        input=open(path)
        print path
        word=load(int(name[:-4]))
        result={}
        for i in word:
            result[i]={}
        for line in input:
            line=line.strip().decode("utf-8")
            if line[:3]==u">>>":
                kind=line.split('/',1)[0][3:]
            else:
                if line in word:
                    try:
                        result[line][kind]+=1
                    except:
                        result[line][kind]=1
        for k,v in result.iteritems():
            output.write("%s\t%s\n"%(
                k,
                " ".join(["%s:%s"%(k,v) for k,v in v.iteritems()])
                )
            )

        input.close()
output.close()