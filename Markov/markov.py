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



def getTMatrix(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        text = word_tokenize(file.read().replace('\n', ' '))
        str = getRidOfPunctuationAndUpperWords(text)

        return computeTMatrix(str)

def calculateProbability(string, TMatrix):
    bigrams = ngrams(string, 2)
    s = 0
    for bigram in bigrams:
        first = bigram[0]
        second = bigram[1]
        p = TMatrix[LetterIndices.index(first), LetterIndices.index(second)]
        s += log0(p)
    return s
def classifyText(filename, TMatrices):
    with open(filename, 'r', encoding = 'utf-8') as file:
        text = word_tokenize(file.read().replace('\n', ' '))
        string = getRidOfPunctuationAndUpperWords(text)
        probabilities = []
        for TMatrix in TMatrices:
            s = calculateProbability(string, TMatrix)
            probabilities.append(s)
        return probabilities

def computeTMatrix(string):
    T = np.zeros([SYMBOLS,SYMBOLS])
    bigrams = ngrams(string, 2)
    for bigram in bigrams:
        first = bigram[0]
        second = bigram[1]
        T[LetterIndices.index(first), LetterIndices.index(second)] += 1

    sums = np.sum(T, axis=1)

    for i in range(SYMBOLS):
        if sums[i] != 0:
            T[i,:]/=sums[i]
    return T

def getRidOfPunctuationAndUpperWords(text): 
    s = ' '.join(text)
    #удаляем пунктуацию
    table = str.maketrans('', '', ',!?.;:\'"`-“‘’0123456789—”…*–()­')
    s = s.translate(table)
    
    return " ".join([w.lower() for w in s.split()])
        

Vonnegut = getTMatrix("Vonnegut1.txt")
Martin = getTMatrix("Martin1.txt")
Lovecraft = getTMatrix("Lovecraft1.txt")
Rowling = getTMatrix("Rowling1.txt")
TMatrices = [Vonnegut, Martin, Lovecraft, Rowling]

print("Английский язык: 1. Воннегут 2. Мартин 3. Лавкрафт 4. Роулинг")
PList = classifyText("Lovecraft2.txt", TMatrices)
print("Лавкрафт", PList)
PList = classifyText("Vonnegut2.txt", TMatrices)
print("Воннегут", PList)
PList = classifyText("Martin2.txt", TMatrices)
print("Мартин", PList)
PList = classifyText("Rowling2.txt", TMatrices)
print("Роулинг", PList)





