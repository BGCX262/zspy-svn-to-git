#coding:utf-8

from zspy.html import abs_href
from zspy.language import abstract
class BasePage(object):
    def __init__(self,url,path=""):
        self.path=path
        self.url=url
        self.content=""
    def write(self,content):
        self.content+=content
    def end(self,downer):
        print self.url
        print self.content[:256]
        print '-'*128
    def parse(self):
        abstract()

class DirPage(BasePage):
    def end(self,downer):
        for url,name in self.parse():
            downer.add(
                self.next_saver(
                    abs_href(url,self.url),
                    "%s/%s"%(self.path,name.replace('/','_'))
                )
            )

class PostListPage(BasePage):
    def end(self,downer):
        for url,name in self.parse():
            url=abs_href(url,self.url)
            if url in downer.history:break
            downer.add(
                self.next_saver(
                    url,
                    "%s/%s"%(self.path,name.replace('/','_'))
                )
            )

class PostPage(BasePage):
    saver=[]
    def parse(self):
        abstract()

    @classmethod
    def add_saver(cls,saver):
        cls.saver.append(saver)

    def end(self,downer):
        parse=self.parse()
        for i in self.saver:
            i(
                self.path,
                parse                
            )