import re
import string
class SentenceComparison:
    '''
        This class represents the comparison of one sentence with another. It produces
        a tree showing the differences. From this can be reconstructed the original
        sentences, showing where the sentences differ.
        Each word in a sentence is atomic.
    '''
    def __init__(self, string1, string2, depth=0, tokenize=str.split):
        '''
            string1: the first sentence
            string2: the second sentence
            If unicode strings are to be used, the tokenize function
            will need to be overridden to be unicode.split
        '''
        DEBUG = False
        if DEBUG:
            print "__init__: depth %s called with %s : %s" % (depth, string1, string2)
        self.tokenize = tokenize
        
        self.string1 = ' '.join(tokenize(string1))
        self.string2 = ' '.join(tokenize(string2))
        
        self.lcs = ""
        self.lTree = None
        self.rTree = None
        self.depth = depth
        
        self._buildTree()
    def _buildTree(self):
        '''
            Based on string1 and string2, build up the (prefix, common, suffix) tree
            structure
        '''
        lTree = None
        rTree = None
        
        string1 = self.string1
        string2 = self.string2
        
        DEBUG = False
        if DEBUG:
            print "_buildTree depth %s: (%s : %s) " % (self.depth, string1, string2),
        if string1 == "":
            if DEBUG:
                print 'a'
            lTree = ""
            rTree = self.string2
            self.lcs = ""
        elif string2 == "":
            if DEBUG: print 'b'
            lTree = self.string1
            rTree = None
            self.lcs = ""
        else: #Both strings contain text
            self.lcs = self.LCS(string1, string2, tokenize=self.tokenize).strip()

            if self.lcs == '':
                lTree = string1
                rTree = string2
            else:
                tuple1 = string1.split(self.lcs, 1)
                if len(tuple1) == 2:
                    prefix1, suffix1 = tuple1
                else:
                    [prefix1] = tuple1
                    suffix1 = ''
                tuple2 = string2.split(self.lcs, 1)
                if len(tuple2) == 2:
                    prefix2, suffix2 = tuple2
                else:
                    [prefix2] = tuple2
                    suffix2 = ''
                lTree = SentenceComparison(prefix1, prefix2, depth=self.depth + 1)
                rTree = SentenceComparison(suffix1, suffix2, depth=self.depth + 1)
        self.lTree = lTree
        self.rTree = rTree
    def LCS(self, string1, string2, tokenize=str.split):
        '''
        Based on string1 and string2, returns the longest
        common substring, on a word-by-word basis using
        a word-matching regular expression.
        '''
        words1 = tokenize(string1)
        words2 = tokenize(string2)
        m = len(words1)
        n = len(words2)
        lengths = [[0] * (n+1) for i in xrange(m+1)]
        LCS = []
        longest = 0
        for i in xrange(m):
            for j in xrange(n):
                if words1[i] == words2[j]:
                    v = lengths[i][j] + 1
                    lengths[i+1][j+1] = v
                    
                    if v > longest: longest = v
                    if v == longest: LCS = words1[i - v+1:i+1]
        return ' '.join(LCS)

    
    def lString(self):
        '''
            Print out the left string, noting additions and removals
        '''
        DEBUG = False
        if DEBUG:
            print "\nlString: (%s : %s)" % (self.string1, self.string2),
        lTree = self.lTree
        rTree = self.rTree
        lcs = self.lcs
        
        myString = ''
        
        if lTree is not None:
            if isinstance(lTree, basestring):
                if lTree is not "":
                    myString += "1\t%s" % (lTree) +"\n"
            else:
                myString += lTree.lString()
        else:
            if DEBUG: print 'lTree is None'
            
        if lcs != "":
            myString = myString
            '''
                Do not show the same part of sentence.
            '''
            '''myString = myString + lcs'''
        if rTree is not None:
            if isinstance(rTree, basestring):
                if rTree is not "":
                    myString += "2\t%s" % (rTree)+"\n"
            else:
                myString += rTree.lString()
        return myString
if __name__ == "__main__":
    for i in range(6,56):        
        string1 = open("C:/research/HIT_QIWEI/data/clean/business/"+str(i)+"-1.txt").read()
        string2 = open("C:/research/HIT_QIWEI/data/clean/business/"+str(i)+"-2.txt").read()
        string3 = open("C:/research/HIT_QIWEI/data/clean/business/"+str(i)+"-3.txt").read()
        string4 = open("C:/research/HIT_QIWEI/data/clean/business/"+str(i)+"-4.txt").read()

        '''string1 = string1.translate(string.maketrans("",""), string.punctuation)
        string2 = string2.translate(string.maketrans("",""), string.punctuation)
        string3 = string3.translate(string.maketrans("",""), string.punctuation)
        string4 = string4.translate(string.maketrans("",""), string.punctuation)'''

        a = SentenceComparison(string1, string2)
        #print a.lString()
        r=open("C:/research/HIT_QIWEI/data/clean/business/diff/"+str(i)+"-1-2.txt","w")
        r.write(a.lString())
        r.close()

        a = SentenceComparison(string1, string3)
        #print a.lString()
        r=open("C:/research/HIT_QIWEI/data/clean/business/diff/"+str(i)+"-1-3.txt","w")
        r.write(a.lString())
        r.close()

        a = SentenceComparison(string1, string4)
        #print a.lString()
        r=open("C:/research/HIT_QIWEI/data/clean/business/diff/"+str(i)+"-1-4.txt","w")
        r.write(a.lString())
        r.close()

        a = SentenceComparison(string2, string3)
        #print a.lString()
        r=open("C:/research/HIT_QIWEI/data/clean/business/diff/"+str(i)+"-2-3.txt","w")
        r.write(a.lString())
        r.close()

        a = SentenceComparison(string2, string4)
        #print a.lString()
        r=open("C:/research/HIT_QIWEI/data/clean/business/diff/"+str(i)+"-2-4.txt","w")
        r.write(a.lString())
        r.close()

        a = SentenceComparison(string3, string4)
        #print a.lString()
        r=open("C:/research/HIT_QIWEI/data/clean/business/diff/"+str(i)+"-3-4.txt","w")
        r.write(a.lString())
        r.close()
        
