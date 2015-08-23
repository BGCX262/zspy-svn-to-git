#!/usr/bin/env python
#coding=utf-8

def preprocess(input,output):
    input=open(input)
    output=open(output,'w')
    keyword="关键词 : "
    for line in input:
        line=line.replace('　',' ').replace('',' ')
        if line[:len(keyword)]==keyword:
            temp=[]
            for i in line.split('\t'):
                i=i.strip()
                if i and i.find('href="')<0:
                    temp.append(i)
                else:
                    pos=i.find('<')+1
                    if pos>0:
                        rpos=i.find('>',pos)
                        if rpos>=0:
                            i=i[pos:rpos]
                            if i:
                                temp.append(i)

            line='\t'.join(temp)
        output.write(line)
    input.close()
    output.close()

preprocess("_all.txt","_all_processed.txt")