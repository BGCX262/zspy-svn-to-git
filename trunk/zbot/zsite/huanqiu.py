#!/usr/bin/env python
#coding=utf-8
from BeautifulSoup import BeautifulSoup,SoupStrainer

from zbot.page_model import PostPage,PostListPage,DirPage
from zspy.filesys import filename


class Page(PostPage):
    def parse(self):
        path=[]
        for i in self.path.split('/'):
            path.append(filename(i))
        path[-1]=filename(path[-1],".htm")
        self.path="/".join(path)

        htm=self.content
        soup=BeautifulSoup(htm)
        main=soup.find('div',{'id':'content'})
        title=main.find("h2").string

        try:
            print title
            print "\n"
        except:
            pass

        
        return {
            "keyword":soup.find('meta',{'name':"Keywords"})['content'],
            "title":title,
            "content":''.join([unicode(i) for i in main.find("div",{"id":"text"}).contents]),
            "url":self.url
        }


class Sub2Index(PostListPage):
    next_saver=Page
    def parse(self):
        href=self.url.split("://")
        href=href[0]+"://"+'/'.join(href[1].split('/')[:2])
        result=[]
        try:
            for ul in BeautifulSoup(self.content).find('div',{'id':"main"}).findAll('ul'):
                result.extend([
                    (a['href'],a.string.replace('&nbsp;',''))
                    for a in ul.findAll("a")
                    if href in a['href']
                ])
        except:
            pass

        return result

class SubIndex(DirPage):
    next_saver=Sub2Index
    def parse(self):
        result=[]
        for a in BeautifulSoup(self.content).find('div',{'id':"booknav"}).find('ul').findAll("a"):
            href=a['href']
            if (self.url in href) and ("/photo" not in href) and ('/cartoon_news' not in href):
                result.append( (href,a.string) )
        return result
            
    
class Index(DirPage):
    next_saver=SubIndex
    def parse(self):
        channel=u"中国 军事 财经 国际 台海 华人 休闲".split(u' ')
        result=[]
        for a in BeautifulSoup(self.content).find('div',{'id':'nav'}).find('ul').findAll("a"):
            name=unicode(a.string)
            if name in channel:
                result.append( (a['href'],name))
        return result



