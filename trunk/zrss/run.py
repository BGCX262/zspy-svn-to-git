#!/usr/bin/env python
#coding=utf-8

from fetch import fetch,local_saver

sci_site=u"""首页头条	http://www.sciencenet.cn/xml/news.aspx?di=0
首页要闻	http://www.sciencenet.cn/xml/news.aspx?di=1
频道要闻	http://www.sciencenet.cn/xml/news.aspx?di=3
一般新闻	http://www.sciencenet.cn/xml/news.aspx?di=4
通知公告	http://www.sciencenet.cn/xml/news.aspx?di=5
新闻评论	http://www.sciencenet.cn/xml/news.aspx?di=6
国际快讯	http://www.sciencenet.cn/xml/news.aspx?di=7
热门论文	http://www.sciencenet.cn/xml/news.aspx?di=8
人才高教	http://www.sciencenet.cn/xml/news.aspx?di=9
生命科学	http://www.sciencenet.cn/xml/field.aspx?di=3
前沿交叉	http://www.sciencenet.cn/xml/field.aspx?di=4
政策管理	http://www.sciencenet.cn/xml/field.aspx?di=5
医药健康	http://www.sciencenet.cn/xml/field.aspx?di=6
基础科学	http://www.sciencenet.cn/xml/field.aspx?di=7
工程技术	http://www.sciencenet.cn/xml/field.aspx?di=8
信息科学	http://www.sciencenet.cn/xml/field.aspx?di=9
资源环境	http://www.sciencenet.cn/xml/field.aspx?di=10
所有文章	http://www.sciencenet.cn/xml/blog.aspx?di=0
学术教育	http://www.sciencenet.cn/xml/blog.aspx?di=1
政策争鸣	http://www.sciencenet.cn/xml/blog.aspx?di=2
历史人文	http://www.sciencenet.cn/xml/blog.aspx?di=3
娱乐生活	http://www.sciencenet.cn/xml/blog.aspx?di=4
人物纪事	http://www.sciencenet.cn/xml/blog.aspx?di=5
图片百科	http://www.sciencenet.cn/xml/blog.aspx?di=6"""
import socket
socket.setdefaulttimeout(10)
for i in sci_site.split('\n'):
    i=i.split('\t')
    fetch(i[1].strip(),local_saver("www.sciencenet.cn.txt","科学网/"+i[0]))
    