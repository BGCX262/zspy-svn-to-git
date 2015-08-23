#coding=utf-8
from __future__ import with_statement

from urllib2 import urlopen
import thread
import logging

logger = logging.getLogger("Down")

class Downer(object):
    def close(self):
        self.history.close()

    def add(self,saver):
        self.history.add(saver)
        self.__start_thread()

    @property
    def active_threads(self):
        return self.__threads

    def __down(self):
        while True:
            try:
                saver=self.history.pop()
            except Exception,e:
                logger.error("[Database] %s %s"%(type(e),e))
                with self.close_lock:
                    self.__threads-=1
                self.__start_thread()
                return
            if saver:
                try:
                    saver.write(urlopen(saver.url).read())
                except Exception, e:
                    logger.error("[NetWork] "+saver.url+" "+str(e))
                    self.history.fail(saver)
                else:
                    try:
                        next=saver.end(self)
                    except Exception, e:
                        logger.error("[Parse] "+saver.url+" "+str(e))
                    self.history.finish(saver)
            else:
                self.close_lock.acquire()
                self.__threads-=1
                self.close_lock.release()
                return

    def __init__(self,history,max_threads=16):
        self.history=history
        self.max_threads=max_threads
        self.__threads=0

        self.close_lock=thread.allocate_lock()

        for i in range(max_threads):
            self.__start_thread()

    def __start_thread(self):
        if self.__threads<self.max_threads:
            self.close_lock.acquire()
            try:
                thread.start_new_thread(self.__down,())
                self.__threads+=1
            finally:
                self.close_lock.release()


