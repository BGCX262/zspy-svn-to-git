#!/usr/bin/env python
#coding=utf-8

from os.path import join
from os import walk,remove
from zspy.filesys import merge


def merge_txt(source,to):
    merge_path=[]
    for root, dirs, files in walk(source,topdown=False):
        root=root.replace("\\",'/')
        if root.count("/")==3:
            for i in files:
                merge_path.append(join(root,i))
        if root.count("/")==2:
            merge_to=join(to,"/".join(root.split("/")[1:]).decode("gbk"))
            print merge_to
            merge(merge_path,merge_to+".txt")
            
merge_txt("www.ilib.cn_C-B.html",u"merge/哲学政法")