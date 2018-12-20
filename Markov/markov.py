import numpy as np
from numpy import log
import nltk
from nltk import word_tokenize
from nltk import ngrams
import string
import re

SYMBOLS = 27

#LetterIndices = [" ","а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ь","ы","ъ","э","ю","я"]
LetterIndices = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def log0(x):
    return 0 if x <= 0 else log(x)


#def compute_text_likelihood(filename, T, dict_rev, histogram, index):
def getTMatrix(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        text = word_tokenize(file.read().replace('\n', ' '))
        str = getRidOfPunctuationAndUpperWords(text)
        #print(str)

        return computeTMatrix(str)

def classifyText(filename, matrix):
    with open(filename, 'r', encoding = 'utf-8') as file:
        text = word_tokenize(file.read().replace('\n', ' '))
        str = getRidOfPunctuationAndUpperWords(text)
        #print(str)
        



def computeTMatrix(string):
    T = np.zeros([SYMBOLS,SYMBOLS])
    bigrams = ngrams(string, 2)
    for bigram in bigrams:

        first = bigram[0]
        second = bigram[1]
        T[LetterIndices.index(first), LetterIndices.index(second)] += 1

    sums = np.sum(T, axis=1)

    return T/sums[:, None]

def getRidOfPunctuationAndUpperWords(text):
    #text.remove(',')
    toDeleteList = (',', '!', '?', '.', ';', ':', '\'', '"', '`')
    

    s = ' '.join(text)
    #удаляем пунктуацию
    table = str.maketrans('', '', ',!?.;:\'"`-“‘’0123456789—”')
    s = s.translate(table)
    
    return " ".join([w.lower() for w in s.split()])
    
    

Vonnegut = getTMatrix("Vonnegut1.txt")
print(Vonnegut)
#Martin = getTMatrix("Martin1.txt")
#Lovecraft = getTMatrix("Lovecraft1.txt")



#Pv = classifyText("Lovecraft2.txt", Vonnegut)





