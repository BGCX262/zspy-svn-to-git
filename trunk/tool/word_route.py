#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
from zcut import hash,cn_word_utf8,load_default

load_default()

def load_stop_word(filename):
    f=open(filename)
    stop_word=set()
    for line in f:
        stop_word.add(line[:-1])
    f.close()
    return stop_word
stop_word=load_stop_word("stop_word.txt")

def phrase(sentence):
    pre=[]
    result=[]
    for i in cn_word_utf8(sentence):
        if i in stop_word or i[-1]=="%":
            pre=[]
            continue
        try:
            float(i)
            pre=[]
            continue
        except:
            pass
        
        try:
            pre.append(i.decode('utf-8'))
            while len(''.join(pre))>9:
                pre.pop(0)
            length=len(pre)
            for i in range(0,length):
                    t=''.join(pre[i:length])
                    if len(t)>1:
                        result.append(t)
        except Exception,e:
            print e
    return result

def line_parse(line):
    result=[]
    if line and line!="-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~":
        line=line.split(':')
        if len(line)>1:
            line[0],line[1]=line[0].strip(),line[1].strip()
            if line[0]=="中文标题" or line[0]=="摘要":
                t=phrase(line[1])
                for i in t:
                    result.append(i)
            elif line[0]=="关键词":
                for i in re.split('\s+',line[1]):
                    result.extend(phrase(i))
    return result

from os import walk,remove
from os.path import join

prime=461
count={}

for root, dirs, files in walk("merge"):
    output=[]
    for number in range(prime):
        output.append(open("output/%s.txt"%number,'a'))
    for name in files:
        path=join(root,name)
        input=open(path)
        
        rel_path='/'.join(path.split('\\')[1:])[:-4].decode("gbk")
        try:
            print rel_path
        except Exception:
            print "oops"
            
        rel_path_0=rel_path.split('/')[0]
        length=0
        for i in output:
            i.write(">>>%s\n"%rel_path)
        for line in input:
            words=line_parse(line)
            if words:
                length+=len(line)
            for word in words:
                output[hash(word[:2].encode('utf-8'),prime)].write("%s\n"%(word))

        input.close()
        remove(path)

        try:
            count[rel_path_0]+=length
        except KeyError:
            count[rel_path_0]=length

    for i in output:
        i.close()

line_no=open("char_number.txt","w")
for k,v in count.iteritems():
    line_no.write("%s\t%s个字\n"%(k,v))
line_no.close()