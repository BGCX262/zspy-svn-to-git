#!/usr/bin/env python
#coding=utf-8
import feedparser
from BeautifulSoup import BeautifulSoup
from os.path import join,dirname

import config
from zspy.html import abs_href,sitename
from zspy.filesys import filename,makedirs

def img_saver(downer,url,html,url_prefix,base_dir=join("img")):
    html=BeautifulSoup(html)
    for i in html.findAll('img'):
        src=i.get('src',None)
        if src:
            url=abs_href(src,url)
            ref=url.split('://')[1]
            i['src']=join(url_prefix,ref)
            downer.add(url,join(base_dir,ref))
    return str(html)

def template_render(c,template_name):
    return config.get_template(template_name).render(**c)

def file_saver(filename,content):
    makedirs(dirname(filename))
    f=open(filename,'w+')      
    f.write(content)
    f.close()

from db import session,News
def db_saver(meta,html):
    session.save(
        News(meta.link,meta.title,html)
    )
    session.commit()

def exist(url):
    if session.query(News).filter_by(url=url).limit(1).first():
        return True
    return False
    
def local_saver(template_name,dirname):
    def _local_saver(downer,meta):
        if exist(meta.link):return
        else:
            print "saveing",meta.link
        meta['summary']=img_saver(downer,meta.link,meta['summary_detail']['value'],"../../img/")
        template_render(meta,template_name)
        c=template_render(meta,template_name)
        file_saver(join(dirname,filename(meta.title)+'.htm'),c)
        db_saver(meta,c)
    return _local_saver

from urllib import URLopener,quote
class Downer:
    def add(self,url,path):
        print "saveing image",url
        makedirs(dirname(path))
        URLopener().retrieve(url.encode('utf-8'),path)

def fetch(url,recall):
    downer=Downer()
    for i in feedparser.parse(url)['entries']:  
        try:
            recall(downer,i)
        except  Exception, e:
            print "[Recall Error]:",e