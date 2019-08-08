from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.corpus import conll2000
import nltk.util
import sys
import urllib2
import os

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def extract_words(text):
    '''
    here we are extracting features to use in our classifier. We want to pull all the words in our input
    porterstem them and grab the most significant bigrams to add to the mix as well.
    '''

    stemmer = PorterStemmer()

    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(text)

    bigram_finder = BigramCollocationFinder.from_words(tokens)
    bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 500)

    for bigram_tuple in bigrams:
        x = "%s %s" % bigram_tuple
        tokens.append(x)

    result =  [stemmer.stem(x.lower()) for x in tokens if x not in stopwords.words('english') and len(x) > 1]
    return result

def get_feature(word):
    return dict([(word, True)])


def bag_of_words(words):
    return dict([(word, True) for word in words])


def create_training_dict(text, sense):
    ''' returns a dict ready for a classifier's test method '''
    tokens = extract_words(text)
    return [(bag_of_words(tokens), sense)]



def run_classifier_tests(classifier):
    testfiles = [{'F': 'C:/research/HIT_QIWEI/data/clean/label/F_r.txt'},
                 {'H': 'C:/research/HIT_QIWEI/data/clean/label/H_r.txt'},
                 {'O': 'C:/research/HIT_QIWEI/data/clean/label/O_r.txt'},
                 {'P': 'C:/research/HIT_QIWEI/data/clean/label/P_r.txt'},
                 {'S': 'C:/research/HIT_QIWEI/data/clean/label/S_r.txt'}
                 ]
    #testfiles = [{'performance': 'http://en.wikipedia.org/wiki/Performance_measurement'},
     #            {'resource': 'http://en.wikipedia.org/wiki/Resource_management'},
      #           {'risk': 'http://en.wikipedia.org/wiki/Risk_management'},
       #          {'strategic': 'http://en.wikipedia.org/wiki/Strategic_alignment'},
        #         {'value': 'http://en.wikipedia.org/wiki/Val_IT'},]
    testfeats = []
    for file in testfiles:
        for sense, loc in file.iteritems():
            for line in open(loc).read():
                testfeats = testfeats + create_training_dict(line, sense)


    acc = accuracy(classifier, testfeats) * 100
    print 'accuracy: %.2f%%' % acc

    #sys.exit()


if __name__ == '__main__':

    # create our dict of training data
    texts = {}
    texts['F'] = 'C:/research/HIT_QIWEI/data/clean/label/F_r.txt'
    texts['H'] = 'C:/research/HIT_QIWEI/data/clean/label/H_r.txt'
    texts['O'] = 'C:/research/HIT_QIWEI/data/clean/label/O_r.txt'
    texts['P'] = 'C:/research/HIT_QIWEI/data/clean/label/P_r.txt'
    texts['S'] = 'C:/research/HIT_QIWEI/data/clean/label/S_r.txt'


    #holds a dict of features for training our classifier
    train_set = []

    # loop through each item, grab the text, tokenize it and create a training feature with it
    for sense, file in texts.iteritems():
        print "training %s " % sense
        text = open(file, 'r').read()
        features = extract_words(text)
        train_set = train_set + [(get_feature(word), sense) for word in features]


    classifier = NaiveBayesClassifier.train(train_set)

    # uncomment out this line to see the most informative words the classifier will use
    classifier.show_most_informative_features(50)


    # uncomment out this line to see how well our accuracy is
    run_classifier_tests(classifier)



    r=open("C:/research/HIT_QIWEI/data/clean/r_diff_class.txt","w")
    for line in open("C:/research/HIT_QIWEI/data/diff/Risk_all_with_wordscount_delete_short.txt", 'r'):
#    for line in open("C:/research/HIT_QIWEI/data/clean/risk/sentences.txt", 'r'):
        tokens = bag_of_words(extract_words(line))
        decision = classifier.classify(tokens)
        result = "%s \t %s" % (decision,line )
        r.write(result)
    r.close()

        #print result

#    k=os.listdir('C:/research/HIT_QIWEI/data/clean/business/initial/')
#    r=open("C:/research/HIT_QIWEI/data/clean/b_class.txt","w")
#    for i in range(0,len(k)):
#        for line in open("C:/research/HIT_QIWEI/data/clean/business/initial/"+k[i], 'r'):
#            tokens = bag_of_words(extract_words(line))
#            decision = classifier.classify(tokens)
#            result=k[i]+" "+decision+"\n"
#            r.write(result)
#    r.close()

	#print k[i]
	
