#coding=utf-8
from __future__ import with_statement

from sqlalchemy import create_engine, MetaData, Table, Column, types
from sqlalchemy.orm import mapper, relation, backref, create_session,sessionmaker
from datetime import datetime
metadata = MetaData()

news_table = Table('news', metadata,
    Column('id', types.Integer, primary_key=True),
    Column('title', types.Text,index=True),
    Column('url', types.Text,index=True),
    Column('create_date', types.DateTime, default=datetime.now),
    Column('content',types.Text),
)
class News(object):
    def __init__(self, url,title,content):
        self.url = url
        self.title=title
        self.content = content

    def __repr__(self):
        return "<Task('%s')>" % (self.url)

import config
engine = create_engine(config.DB)
metadata.bind=engine
metadata.create_all() 

session = sessionmaker(bind=engine,transactional=True)()
mapper(News,news_table)

