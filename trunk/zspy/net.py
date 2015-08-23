#coding=utf-8

import threading
from cStringIO import StringIO

import pycurl
"""
Asyn open url
Author:zsp007@gmail.com
2008-1-25 17:14
"""

class UrlOpen(threading.Thread):
    """异步下载网页"""

    def __init__(self,):
        super(UrlOpen,self).__init__()
        self.opener = pycurl.CurlMulti()
        self.handle_list=[]
        self.waiting=[]
        self._close=False

    def add(self,url,recall,catch=None,writer=StringIO()):
        """
        参数:网址,回调函数,存放临时数据的对象
        """
        if catch is None:
            def catch(curl,error_no,desp):
                print "Error:%s - %s"%(error_no,desp)
                #pass

        c = pycurl.Curl()

        #可以传给回调函数
        c.url=url
        c.content = writer
        c.recall = recall
        c.catch=catch
        c.setopt(c.URL,
            url.encode('utf-8') if type(url) is unicode else url
        )
        c.setopt(c.WRITEFUNCTION,c.content.write)
        self.waiting.append(c)

    def _add(self):
        size=1-len(self.handle_list)
        if size>0:
            waiting=self.waiting[:1]
            self.waiting=self.waiting[1:]
            for c in waiting:
                self.handle_list.append(c)
                self.opener.add_handle(c)

    def open(self,url,recall):
        self.add(url,lambda c:recall(c.content.getvalue()))

    def _remove(self,c):
        c.close()
        self.opener.remove_handle(c)
        self.handle_list.remove(c)

    def close(self):
        self._close=True

    def run(self):
        import select
        import time
        num_handle=0
        while 1:
            self._add()
            if self.handle_list:
                ret = self.opener.select(1.0)
                if ret >= 0:
                    while 1:
                        num_handle_pre=num_handle
                        ret, num_handle =self.opener.perform()
                        #活动的连接数改变时
                        if num_handle!=num_handle_pre:
                            result=self.opener.info_read()
                            for i in result[1]:
                                #成功
                                i.http_code = i.getinfo(i.HTTP_CODE)
                                self._remove(i)
                                i.recall(i)
                            for i in result[2]:
                                #失败,应该记录一下,或回调失败函数
                                #i为(<pycurl.Curl object at 0x00C04C80>, 6, 'Could not resolve host: www.msn.com (Domain name not found)')
                                i[0].catch(*i)
                                self._remove(i[0])
                        if ret != pycurl.E_CALL_MULTI_PERFORM:
                            break
            else:
                if self._close == True:
                    self._Thread__stop()
                time.sleep(1)

if __name__=="__main__":
    def show(x):
        print x.content.getvalue()
        print '--'*11

    opener=UrlOpen()
    opener.start()
    opener.add("http://www.baidu.com/",show)
    opener.add("http://www.google.com/",show)
    opener.close()
