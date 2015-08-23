#!/usr/bin/env python
#coding=utf-8
from BeautifulSoup import BeautifulSoup,SoupStrainer

from zbot.page_model import PostListPage,PostPage
from zspy.filesys import filename

class Page(PostPage):
    def parse(self):
        path=[]
        for i in self.path.split('/'):
            path.append(filename(i))
        path[-1]=filename(path[-1].split(' ',2)[0]+".htm")
        self.path="/".join(path)
        
        htm=self.content
        soup=BeautifulSoup(htm)
        title=soup.find('div',{'id':'artibodyTitle'}).find("h1").string

        content=''.join([unicode(i) for i in soup.find("div",{"id":"artibody"}).contents])


        try:
            print title
            print "\n"
        except:
            pass
        return {
            "url":self.url,
            "title":title,
            "content":content
        }

class Index(PostListPage):
    next_saver=Page
    def parse(self):
        result=[]
        for ul in BeautifulSoup(self.content).find('div',{'class':'M_Right'}).findAll('ul'):
            result.extend([
                (i['href'],i.string) for i in ul.findAll('a')
            ])
        return result



