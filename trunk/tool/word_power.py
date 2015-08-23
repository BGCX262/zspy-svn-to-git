from math import sqrt,log,pow

all_medicine=40083272
all_other=48704735
all_word=all_other+all_medicine

keywords=[]

for line in open("kind_count.txt"):
    word,medicine,other=line.strip().split('\t')
    medicine=int(medicine.split(':')[1])
    other=int(other.split(':')[1])
    all=medicine+other
    p_medicine=float(medicine)/all_medicine
    p_other=float(other)/all_other
    p_avg=(p_medicine+p_other)/2
    if p_medicine>=0.000001 and 2*p_other<p_medicine:
        power=sqrt(
            sqrt((p_medicine-p_avg)**2+(p_other-p_avg)**2)/(p_medicine+p_other)
        )*((log(all)-log(all_word))**2)*pow(p_medicine,.125)
        if power>0:
            keywords.append((word,power))

keywords.sort(lambda x,y:cmp(y[1],x[1]))

for k,v in keywords:
    print k,v