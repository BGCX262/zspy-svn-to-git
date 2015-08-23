#!/usr/bin/env python
#coding=utf-8
from BeautifulSoup import BeautifulSoup,SoupStrainer

from zbot.page_model import PostPage,DirPage
from zspy.filesys import filename

class Page(PostPage):
    def parse(self):
        path=[]
        for i in self.path.split('/'):
            path.append(filename(i))
        path[-1]=filename(path[-1].split(' ',2)[0]+".txt")
        self.path="/".join(path).decode('utf-8')
        htm=self.content
        soup=BeautifulSoup(htm)
        cn_title=soup.find('h1').find("span",{"id":"ctl00_MasterContentPlaceHolder_TitleLabel"}).string
        en_title=soup.find('h2').find("span").string
        if not en_title:
            en_title=""
        from zspy.html2txt import html2txt
        brief=soup.find("span",{"id":"ctl00_MasterContentPlaceHolder_AbstractLabel"}).string
        if brief:
            brief=html2txt(brief)
        else:brief=""

        page_author=soup.find("span",{"id":"ctl00_MasterContentPlaceHolder_AuthorDataList"})
        if page_author:
            author='\t'.join(
            [i.string for i in page_author.findAll('a')]
            )
        else:author=''
        page_word=soup.find("span",{"id":"ctl00_MasterContentPlaceHolder_KeywordDatalist"})
        if page_word:
            page_word=page_word.findAll('a')
        else:
            page_word=[]
        keyword='\t'.join([
            i.string
            for i in page_word
        ])
        
        magezine=soup.find("a",{"id":"ctl00_MasterContentPlaceHolder_PeriodicalLink"}).string
        time=soup.find("a",{"id":"ctl00_MasterContentPlaceHolder_IssueLink"}).string
        kind=' >>> '.join([
            soup.find("a",{"id":"ctl00_MasterContentPlaceHolder_topnavigation"}).string,
            soup.find("a",{"id":"ctl00_MasterContentPlaceHolder_subnavigation"}).string
        ])

        return {
            "url":self.url,
            "cn_title":cn_title,
            "en_title":en_title,
            "keyword":keyword,
            "author":author,
            "magezine":magezine,
            "time":time,
            "kind":kind,
            "brief":brief.replace('" class="highLight">','')
        }

class PaperIndex(DirPage): 
    next_saver=Page
    def parse(self):
        return [
                (i['href'],i.string)
                for i in BeautifulSoup(self.content).findAll("a",{'class':'highLight'})
        ]



class PeriodicalIndex(DirPage):
    next_saver=PaperIndex
    def parse(self):
        htm=self.content
        begin=htm.find("<div>",htm.find('收录汇总'))+len("<div>")
        htm=htm[begin:htm.find("</div>",begin) ]
        return [
            (i['href'],i['href'].split('.',2)[1]+'_'+i.string)
            for i in BeautifulSoup(htm).findAll("a")
        ]


class MagazineIndex(DirPage):
    next_saver=PeriodicalIndex
    def parse(self):
        return [
                (i['href'],i.string)
                for i in BeautifulSoup(self.content).findAll("a",{'class':'highLight'})
        ]


class KindIndex(DirPage):
    next_saver=MagazineIndex
    def parse(self):
        return [
            (i['href'],i.string)
            for i in BeautifulSoup(self.content).findAll("a",{'class':'highLight'})
        ]

class Index(DirPage):
    next_saver=KindIndex
    def parse(self):
        result=[
            (i['href'],i.string)
            for i in BeautifulSoup(
                    self.content,
                    parseOnlyThese=SoupStrainer('td')
            ).findAll('a',{'class':'highLight'})
        ]
        return result



