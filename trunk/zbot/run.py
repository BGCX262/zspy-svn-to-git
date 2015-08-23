from os.path import join

import config
from env import Env

Env.load(config)

def load_db(site_name):
    db_path=join(config.SQLDB,site_name+'.sqlite')
    
    from sqlalchemy import create_engine
    engine = create_engine(db_path)
    from downtask_sqlite import DownTask
    task=DownTask(engine)
    task.reset_downing()
    return task

def site(index_url,parser,once=True):
        
    from zspy.filesys import makedirs,filename

    site_name=filename(index_url.split("://",2)[1])
    task=load_db(site_name)

    from down import Downer
    downer=Downer(task)
    
    if once and index_url in downer.history:
        print "Continue %s"%index_url
    else:
        print "New Start %s"%index_url        
        downer.add(
            parser(
                index_url,
                "%s/%s"%(
                    config.FETCH_TO,
                    site_name
                )
            )
        )
    return downer

from saver import mako_render

#from zsite import ilib
#ilib.Page.add_saver(mako_render("ilib.txt"))
#downer=site("http://www.ilib.cn",ilib.Index)
#downer=site("http://www.ilib.cn/C-R.html",ilib.KindIndex)


#from zsite import sina_olympic
#sina_olympic.Page.add_saver(mako_render("2008.sina.com.cn.txt"))
#downer=site("http://2008.sina.com.cn/news/act/index.shtml",sina_olympic.Index,False)
#downer=site("http://2008.sina.com.cn/news/news",sina_olympic.Index,False)

#from zsite import huanqiu
#huanqiu.Page.add_saver(mako_render("huanqiu.com.txt"))
#downer=site("http://www.huanqiu.com",huanqiu.Index,False)

from zsite import dangdang
ilib.Page.add_saver(mako_render("dangdang.txt"))
downer=site("http://zspy.googlecode.com/svn/trunk/zbot/zsite/dangdang.txt",dangdang.Index)

import time
count=0
while True:
    try:
        at_num=downer.active_threads
        if not at_num:break
        count+=1
        print "count:%s\tdowner.active_threads:%s"%(count,downer.active_threads)
        time.sleep(10)
    except KeyboardInterrupt:
        downer.close()
        Env.db_env.close()
        print "88!"
        break