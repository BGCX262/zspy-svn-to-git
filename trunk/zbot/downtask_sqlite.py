#coding=utf-8
from __future__ import with_statement

from sqlalchemy import create_engine, MetaData, Table, Column, types
from sqlalchemy.orm import mapper, relation, backref, create_session,sessionmaker
import cPickle as pickle
import thread



class DownState:
    to_down=0
    downing=1

class DownTask(object):
    metadata = MetaData()

    task_table = Table('users', metadata,
        Column('id', types.Integer, primary_key=True),
        Column('url', types.Text,index=True),
        Column('recall', types.Binary),
        Column('state',types.Integer,index=True),
    )

    class Task(object):
        def __init__(self, url, recall,state=DownState.to_down):
            self.url = url
            self.recall = pickle.dumps(recall)
            self.state=state
        def __repr__(self):
            return "<Task('%s')>" % (self.url)

    def __init__(self,engine):
        self.metadata.bind=engine
        self.__session = sessionmaker(bind=engine,transactional=True)       
        mapper(self.Task,self.task_table)

        self._db_lock=thread.allocate_lock()
        self._db_closed=False
        self.metadata.create_all() 
    
    @property
    def session(self):
        return self.__session()
    
    def close(self):
        """关闭数据库"""
        from sqlalchemy.orm import clear_mappers
        clear_mappers()

    def __contains__(self,url):
        return True if self.session.query(self.Task).limit(1).first() else False

    def add(self,saver):
        ss=self.session
        with self._db_lock:
            ss.save(
                self.Task(saver.url,saver)
            )
            ss.commit()
            ss.close()

    def pop(self):
        ss=self.session
        with self._db_lock:
            saver=ss.query(self.Task).filter_by(state=DownState.to_down).limit(1).order_by(self.Task.id.desc()).first()
            if saver:
                saver.state=DownState.downing
                ss.update(saver)
                ss.commit()
            ss.close()
        result=pickle.loads(str(saver.recall)) if saver else None
        return result

    def reset_downing(self):
        ss=self.session
        with self._db_lock:
            for i in ss.query(self.Task).filter_by(state=DownState.downing).all():
                i.state=DownState.to_down
                ss.update(i)
                ss.commit()
                ss.close()

    def finish(self,saver):
        self.__over(saver)

    def fail(self,saver):
        self.__over(saver)

    def __over(self,saver):
        ss=self.session
        with self._db_lock:
            saver=ss.query(self.Task).filter_by(url=saver.url).limit(1).first()
            if saver:
                ss.delete(saver)
                ss.close()
