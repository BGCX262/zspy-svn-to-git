from cn_word import cn_word_utf8,load_dict


import time

begin=time.time()

load_dict("dict.txt")

print "Load Dictionary Cost Time %ssec\n"%(time.time()-begin)

begin=time.time()

for i in open("test.txt"):
    print ' '.join(cn_word_utf8(i)).decode('utf-8'),


print "\n\nCost Time %ssec"%(time.time()-begin)