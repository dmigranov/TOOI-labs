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
    properties = []
    def __init__(self, text):
        self.text = text
    def addProperty(self, p):
        self.properties.append(p)
        

class Sentence:
    sentence = []

    def addWord(self, w):
        self.sentence.append(w)
        
class Corpus:
    corpus = []

    def addSentence(self, s):
        self.corpus.append(s)
    def getWord(self, sentenceNumber, wordNumber):
        return corpus.corpus[sentenceNumber].sentence[wordNumber].text
        

import xml.etree.ElementTree as etree
tree = etree.parse('file.xml')
root = tree.getroot()

corpus = Corpus()
for tokens in root.iter('tokens'):
    s = Sentence()
    for token in tokens:
        w = Word(token.find('tfr').find('v').find('l').get('t'))
        #print(token.find('tfr').find('v').find('l').get('t'))
        for g in token.iter('g'):
            w.addProperty(g.get('v'))
        s.addWord(w)
    corpus.addSentence(s)
            
print(corpus.getWord(0,1))


