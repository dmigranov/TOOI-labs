import numpy as np
from numpy import log
import nltk
from nltk import word_tokenize
from nltk import ngrams
import string

SYMBOLS = 27

#LetterIndices = [" ","а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ь","ы","ъ","э","ю","я"]
LetterIndices = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def log0(x):
    return 0 if x <= 0 else log(x)


#def compute_text_likelihood(filename, T, dict_rev, histogram, index):
def compute_text_likelihood(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        text = word_tokenize(file.read().replace('\n', ' '))
        str = getRidOfPunctuationAndUpperWords(text)
        print(str)
        computeTMatrix(str)

def classify_text(tmatrices, dict_revs, histograms, filename):
    print(0)

def computeTMatrix(string):
    T = np.zeros([SYMBOLS,SYMBOLS])
    bigrams = ngrams(string, 2)
    for bigram in bigrams:

        first = bigram[0]
        second = bigram[1]
        T[LetterIndices.index(first), LetterIndices.index(second)] += 1
    print(T)

def getRidOfPunctuationAndUpperWords(text):
    #text.remove(',')
    toDeleteList = (',', '!', '?', '.', ';', ':', '\'', '"', '`')
    #удаляем пунктуацию
    #for punct in toDeleteList:
        #while punct in text:
            #text.remove(punct)
    for w in text:
        if w[0].isupper():
            while w in text:
                text.remove(w)
    s = ' '.join(text)
    table = str.maketrans('', '', ',!?.;:\'"`-“‘’')
    s = s.translate(table)
    
    return " ".join(s.split())
    
    

compute_text_likelihood("text.txt")
