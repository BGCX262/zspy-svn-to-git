#coding:utf-8
from os.path import join,dirname

root=dirname(__file__)

MAKO_TEMPLATE_DIR=[
    join(root,'template'),
]
MAKO_MODULE_DIR=join(root,'tmp/mako')

LOGGING_CONFIG="log_conf.ini"

BSDDB_ENV="bsddb"

FETCH_TO="fetched_page"

SQLDB="sqlite:///sqlite_db/"



