import nltk
import os
import glob

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

path = 'C:/research/HIT_QIWEI/data/clean/risk/initial'
for infile in glob.glob( os.path.join(path, '*.txt') ):
    f=open(infile).read()
    sents=tokenizer.tokenize(f)
    local=open("C:/research/HIT_QIWEI/data/clean/risk/sentences.txt", "a")
    for s in sents:
        if len(s)<300:
            x="["+str(infile)+"]"+"\t"+s+"\n"
        local.write(x)
    local.close()
