import xml.etree.ElementTree as etree
import collections
import math

class TFIDF_calculator:
    def __init__(self, filename):
        f = open(filename, 'r', encoding = 'utf-8')
        self.__documents = list()
        self.__words = list()
        self.__IDF = collections.Counter()
        self.__TF = collections.Counter()
        #размера как у set(words)
        self.__getDocuments()
        self.__getWords(f)
        self.__calculateIDF() #если не уже
        self.__calculateTF()
    def __getDocuments(self):
        tree = etree.parse('file.xml')
        root = tree.getroot()
        for paragraphs in root.iter('paragraphs'):
            document = list()
            for token in paragraphs.iter('token'):
                flag = True
                word = token.get("text")
                for g in token.iter('g'):
                    if g.get('v') == "PNCT" or g.get('v') == "UNKN":
                        flag = False
                if flag:
                    document.append(word.lower())
            self.__documents.append(document)
            #for word in document:
                #print(word)
        #print(len(self.__documents))
    def __getWords(self, f):
        
        for line in f:
            words = line.replace(',',' ').replace('.',' ').replace(';',' ').split()
            for w in words:
                self.__words.append(w)
    def __calculateIDF(self):


        
        
        for word in (set(w.lower() for w in self.__words)):
            #count = 0
            for document in self.__documents:
                if word in document:
                    self.__IDF[word] += 1
            if self.__IDF[word] != 0:
                self.__IDF[word] = math.log10(len(self.__documents) / self.__IDF[word])
        #print(self.__IDF)
        
    def __calculateTF(self):
        counter = collections.Counter()
        for word in self.__words:
            w = word.lower()
            counter[w] += 1

        for word in (set(w.lower() for w in self.__words)):

            self.__TF[word] = counter[word] / len(self.__words)
        #print(self.__TF)


    def getTFIDF(self):
        TFIDF = collections.Counter()
        for word in (set(w.lower() for w in self.__words)):
            TFIDF[word] = self.__TF[word] * self.__IDF[word]
        return TFIDF
            



tfidf = TFIDF_calculator('my.txt')
print(tfidf.getTFIDF())
