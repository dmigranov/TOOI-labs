#1, 2
class A:
    c = 0
    def __init__(self, a):
        self.a = a
        c = -a
        
    def setB(self, b):
        b.b = self.a

class B:
    def __init__(self, b):
        self.b = b


a1 = A(7)
a2 = A(6)
b1 = B(4)
print(a1.a)
print(b1.b)

a1.setB(b1)
print(a1.a)
print(b1.b)


#3

class Word:

    def __init__(self, text, lemma):
        self.properties = list()
        self.text = text
        self.lemma = lemma
    def addProperty(self, p):
        self.properties.append(p)
        

class Sentence:

    def __init__(self):
        self.words = list()
    def addWord(self, w):
        self.words.append(w)
    def printSentence(self):
        for word in words:
            print (word.text)
        
class Corpus:


    def __init__(self):
        self.sentences = list()
    def addSentence(self, s):
        self.sentences.append(s)
    def getWord(self, sentenceNumber, wordNumber):
        return self.sentences[sentenceNumber].words[wordNumber].text
    def printWord(self, sentenceNumber, wordNumber):
        print(self.getWord(sentenceNumber, wordNumber))
        for p in self.sentences[sentenceNumber].words[wordNumber].properties:
            print(p)
        

import xml.etree.ElementTree as etree
tree = etree.parse('file.xml')
root = tree.getroot()

corpus = Corpus()
for sentence in root.iter('sentence'):
    s = Sentence()
    #print('here')
    tokens = sentence.find('tokens')

    for token in tokens:
        w = Word(token.get('text'), token.find('tfr').find('v').find('l').get('t'))
        for g in token.find('tfr').find('v').find('l').findall('g'):
            w.addProperty(g.get('v'))
            #w.properties.append(g.get('v'))
        s.addWord(w)
        #s.words.append(w)
        
    #s.printSentence()
    corpus.addSentence(s)
    #corpus.sentences.append(s)

            
#print(corpus.sentences[5].words[2].text)
corpus.printWord(5,1)


