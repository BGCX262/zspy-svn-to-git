#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
total_count={}
for line in open("count.txt"):
    path,count=line.split(' ',1)
    total_count["path"]=total_count.get("path",0)+int(count)
for k,v in total_count.iteritems():
    print k,v