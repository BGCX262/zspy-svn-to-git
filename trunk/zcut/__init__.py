#coding=utf-8
from cn_word import add_word,cn_word_utf8,hash

def load_dict(txt):
    f=open(txt)
    for line in f:
        add_word(line.strip())
    f.close()

def load_default():
    import os
    load_dict(os.path.join(os.path.dirname(__file__),"dict.txt"))
