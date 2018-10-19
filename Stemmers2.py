Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.book import text1
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> tex2

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tex2
NameError: name 'tex2' is not defined
>>> 
KeyboardInterrupt
>>> text2

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    text2
NameError: name 'text2' is not defined
>>> text1
<Text: Moby Dick by Herman Melville 1851>
>>> from nltk.book import *
>>> from nltk.book import *
>>> text2
<Text: Sense and Sensibility by Jane Austen 1811>
>>> text = text4[500:600]
>>> print(' '.join(text))
citizens at large less than either . No people can be bound to acknowledge and adore the Invisible Hand which conducts the affairs of men more than those of the United States . Every step by which they have advanced to the character of an independent nation seems to have been distinguished by some token of providential agency ; and in the important revolution just accomplished in the system of their united government the tranquil deliberations and voluntary consent of so many distinct communities from which the event has resulted can not be compared with the means by which most
>>> port = nltk.stem.porter.PorterStemmer()
>>> text_port = [port.stem(word) for word in text]
>>> print("Porter stemmer:", ' '.join(text_port))
('Porter stemmer:', u'citizen at larg less than either . No peopl can be bound to acknowledg and ador the invis hand which conduct the affair of men more than those of the unit state . everi step by which they have advanc to the charact of an independ nation seem to have been distinguish by some token of providenti agenc ; and in the import revolut just accomplish in the system of their unit govern the tranquil deliber and voluntari consent of so mani distinct commun from which the event ha result can not be compar with the mean by which most')
>>> snowball = nltk.stem.snowball.SnowballStemmer(language = 'english')
>>> text_snowball = [snowball.stem(word) for word in text]
>>> print("Snowball stemmer: ", ' '.join(text_snowball))
('Snowball stemmer: ', u'citizen at larg less than either . no peopl can be bound to acknowledg and ador the invis hand which conduct the affair of men more than those of the unit state . everi step by which they have advanc to the charact of an independ nation seem to have been distinguish by some token of providenti agenc ; and in the import revolut just accomplish in the system of their unit govern the tranquil deliber and voluntari consent of so mani distinct communiti from which the event has result can not be compar with the mean by which most')
>>> lancaster = nltk.stem.lancaster.LancasterStemmer()
>>> text_lanc = [lancaster.stem(word) for word in text]
>>> print('Paice/Husk stemmer:', ' '.join(text_lanc))
('Paice/Husk stemmer:', u'cit at larg less than eith . no peopl can be bound to acknowledg and ad the invis hand which conduc the affair of men mor than thos of the unit stat . every step by which they hav adv to the charact of an independ nat seem to hav been distinct by som tok of provid ag ; and in the import revolv just accompl in the system of their unit govern the tranquil delib and volunt cons of so many distinct commun from which the ev has result can not be comp with the mean by which most')
>>> from nltk.stem import WordNetLemmatizer
>>> wnl = WordNetLemmatizer()
>>> text_wnl = [wnl.lemmatize(word) for word in text]


>>> print('WordNet lemmatizer:', ' '.join(text_wnl))
('WordNet lemmatizer:', u'citizen at large le than either . No people can be bound to acknowledge and adore the Invisible Hand which conduct the affair of men more than those of the United States . Every step by which they have advanced to the character of an independent nation seems to have been distinguished by some token of providential agency ; and in the important revolution just accomplished in the system of their united government the tranquil deliberation and voluntary consent of so many distinct community from which the event ha resulted can not be compared with the mean by which most')
>>> Porter_MVC = 1.0*len(set(text))/len(set(text_port))
>>> Porter_MVC
1.0140845070422535
>>> Lancaster_MVC = 1.0*len(set(text))/len(set(text_lanc))
>>> Snow_MVC = 1.0*len(set(text))/len(set(text_snowball))
>>> wordnet_MVC = 1.0*len(set(text))/len(set(text_wnl))
>>> Lancaster_MVC
1.0285714285714285
>>> Snow_MVC
1.0140845070422535
>>> wordnet_MVC
1.0
>>> Porter_ICF = 1.0*(len(set(text)) - len(set(text_port)))/len(set(text))
>>> Porter_ICF
0.013888888888888888
>>> Lancaster_ICF = 1.0*(len(set(text)) - len(set(text_lanc)))/len(set(text))
>>> Snow_ICF = 1.0*(len(set(text)) - len(set(text_snowball)))/len(set(text))
>>> wordnet_ICF = 1.0*(len(set(text)) - len(set(text_wnl)))/len(set(text))
>>> Lancaster_

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    Lancaster_
NameError: name 'Lancaster_' is not defined
>>> Lancaster_ICF
0.027777777777777776
>>> Snow_ICF
0.013888888888888888
>>> wordnet_ICF
0.0
>>> 
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "C:\Python27\lib\idlelib\rpc.py", line 235, in asyncqueue
    self.putmessage((seq, request))
  File "C:\Python27\lib\idlelib\rpc.py", line 334, in putmessage
    raise IOError, "socket no longer exists"
IOError: socket no longer exists
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "C:\Python27\lib\idlelib\rpc.py", line 235, in asyncqueue
    self.putmessage((seq, request))
  File "C:\Python27\lib\idlelib\rpc.py", line 334, in putmessage
    raise IOError, "socket no longer exists"
IOError: socket no longer exists
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "C:\Python27\lib\idlelib\rpc.py", line 235, in asyncqueue
    self.putmessage((seq, request))
  File "C:\Python27\lib\idlelib\rpc.py", line 334, in putmessage
    raise IOError, "socket no longer exists"
IOError: socket no longer exists
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "C:\Python27\lib\idlelib\rpc.py", line 235, in asyncqueue
    self.putmessage((seq, request))
  File "C:\Python27\lib\idlelib\rpc.py", line 334, in putmessage
    raise IOError, "socket no longer exists"
IOError: socket no longer exists
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "C:\Python27\lib\idlelib\rpc.py", line 235, in asyncqueue
    self.putmessage((seq, request))
  File "C:\Python27\lib\idlelib\rpc.py", line 334, in putmessage
    raise IOError, "socket no longer exists"
IOError: socket no longer exists
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "C:\Python27\lib\idlelib\rpc.py", line 235, in asyncqueue
    self.putmessage((seq, request))
  File "C:\Python27\lib\idlelib\rpc.py", line 334, in putmessage
    raise IOError, "socket no longer exists"
IOError: socket no longer exists
>>> 
KeyboardInterrupt
>>> 
IDLE internal error in runcode()
Traceback (most recent call last):
  File "C:\Python27\lib\idlelib\rpc.py", line 235, in asyncqueue
    self.putmessage((seq, request))
  File "C:\Python27\lib\idlelib\rpc.py", line 334, in putmessage
    raise IOError, "socket no longer exists"
IOError: socket no longer exists
>>> 
