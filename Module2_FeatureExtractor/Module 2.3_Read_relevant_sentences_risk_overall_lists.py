import nltk
import os
import glob

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

i=0
f=set(line.strip() for line in open('c:/calc/overall_set.txt'))

path = 'c:/calc/sample'

local=open("c:/calc/risk_sents.txt", "a")
for infile in os.listdir(path):
    file=open(path+'/'+infile).read()
    sents=tokenizer.tokenize(file.decode('utf-8'))

    
    for sent in sents:
        if len(sent)<300 and len(sent)>50:
            for k in f:
                if k in sent:
                    sent=sent.replace('\n',' ')
                    local.write(k+'\t'+infile+'\t|||'+sent.encode('utf8')+'|||\n')
            

local.close()


