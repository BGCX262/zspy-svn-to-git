#coding:utf-8


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from os.path import join,dirname



MAKO_TEMPLATE_DIR=[
    'template',
]
MAKO_MODULE_DIR=join('tmp/mako')

from mako.lookup import TemplateLookup
get_template = TemplateLookup(
    directories=MAKO_TEMPLATE_DIR,
    module_directory=MAKO_MODULE_DIR,
    output_encoding='utf-8'
).get_template

DB="sqlite:///news.db3"