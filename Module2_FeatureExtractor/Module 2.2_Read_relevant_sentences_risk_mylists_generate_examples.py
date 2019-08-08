import nltk
import os
import glob

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')



path = 'f:/10k/clean'
i=0
f=set(line.strip() for line in open('f:/10k/set/risk_financial_set.txt'))
h=set(line.strip() for line in open('f:/10k/set/risk_hazard_set.txt'))
o=set(line.strip() for line in open('f:/10k/set/risk_operational_set.txt'))
s=set(line.strip() for line in open('f:/10k/set/risk_strategic_set.txt'))



for infile in glob.glob( os.path.join(path, '*.txt') ):
    i=i+1
    file=open(infile).read()
    sents=tokenizer.tokenize(file.decode('utf-8'))
##    local_f=open("C:/research/HIT_QIWEI/data/clean/label/risk_financial.txt", "a")
##    local_h=open("C:/research/HIT_QIWEI/data/clean/label/risk_hazard_set.txt", "a")
##    local_o=open("C:/research/HIT_QIWEI/data/clean/label/risk_operational_set.txt", "a")
##    local_s=open("C:/research/HIT_QIWEI/data/clean/label/risk_strategic_set.txt", "a")
    local=open("f:/10k/risk_examples.txt", "a")
    list_f=[]
    list_h=[]
    list_o=[]
    list_s=[]
    for sent in sents:
        if len(sent)<300 and len(sent)>50:
            for k in f:
                if k in sent:
                    list_f.append(sent)
            for k in h:
                if k in sent:
                    list_h.append(sent)
            for k in o:
                if k in sent:
                    list_o.append(sent)
            for k in s:
                if k in sent:
                    list_s.append(sent)
                    
    for s in set(list_f):
        x="["+str(infile)+"]"+"\t"+"f"+"\t"+s+"|||\n"
        local.write(x.encode("utf8"))
    for s in set(list_h):
        x="["+str(infile)+"]"+"\t"+"h"+"\t"+s+"|||\n"
        local.write(x.encode("utf8"))
    for s in set(list_o):
        x="["+str(infile)+"]"+"\t"+"o"+"\t"+s+"|||\n"
        local.write(x.encode("utf8"))
    for s in set(list_s):
        x="["+str(infile)+"]"+"\t"+"s"+"\t"+s+"|||\n"
        local.write(x.encode("utf8"))

    local.close()
    if i%100==0:
        print i

