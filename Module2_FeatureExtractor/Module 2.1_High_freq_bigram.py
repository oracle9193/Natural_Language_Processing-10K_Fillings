import nltk
from collections import Counter
from nltk import stem
raw = open('f:/10k/risk_examples.txt').read()
stemmer=stem.snowball.EnglishStemmer()

tokens = nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(raw)

tokens_l= [x.lower() for x in tokens]

pairs = nltk.bigrams(tokens_l)

c = Counter(pairs)
a= c.most_common(100000)

w=open('f:/10k/risk_examples_high_freq_bigram_1.txt','w')
f=set(line.strip() for line in open('C:/Dropbox/Rong_Manlu/most_common_words_risk_extend.txt'))
#st=set(line.strip() for line in open('C:/Dropbox/Rong_Manlu/stemmed_unigram.txt'))
risk_list=set(line.strip() for line in open('C:/Dropbox/Rong_Manlu/risk_related_words.txt'))
st=[]

s=set(line.strip() for line in open('C:/Dropbox/Rong_Manlu/stop.txt'))
for word in risk_list:
	st.append(stemmer.stem(word))


for line in a:
    try:
        if (stemmer.stem(unicode(line[0][0], 'ascii', 'ignore')) in st or stemmer.stem(unicode(line[0][1], 'ascii', 'ignore')) in st) and (unicode(line[0][0], 'ascii', 'ignore') not in s) and (unicode(line[0][1], 'ascii', 'ignore') not in s) and (len(unicode(line[0][0], 'ascii', 'ignore')) >1) and (len(unicode(line[0][1], 'ascii', 'ignore')) >1):
            x=unicode(line[0][0], 'ascii', 'ignore')+"\t"+unicode(line[0][1], 'ascii', 'ignore')+"\t"+"|||"+stemmer.stem(unicode(line[0][0], 'ascii', 'ignore'))+"\t"+ stemmer.stem(unicode(line[0][1], 'ascii', 'ignore'))+"\t"+str(line[1])+"|||\n"
            w.write(x)
    except UnicodeDecodeError:
        print 'error'
w.close()
