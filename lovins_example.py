Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
======================== RESTART: D:/Python/lovins.py ========================
>>> lovins_stem("killer")
'killer'
>>> lovins_stem("killers")
'killer'
>>> lovins_stem("defines")
'def'
>>> text = "citizens at large less than either . No people can be bound to acknowledge and adore the Invisible Hand which conducts the affairs of men more than those of the United States . Every step by which they have advanced to the character of an independent nation seems to have been distinguished by some token of providential agency ; and in the important revolution just accomplished in the system of their united government the tranquil deliberations and voluntary consent of so many distinct communities from which the event has resulted can not be compared with the means by which most".split()
>>> text
['citizens', 'at', 'large', 'less', 'than', 'either', '.', 'No', 'people', 'can', 'be', 'bound', 'to', 'acknowledge', 'and', 'adore', 'the', 'Invisible', 'Hand', 'which', 'conducts', 'the', 'affairs', 'of', 'men', 'more', 'than', 'those', 'of', 'the', 'United', 'States', '.', 'Every', 'step', 'by', 'which', 'they', 'have', 'advanced', 'to', 'the', 'character', 'of', 'an', 'independent', 'nation', 'seems', 'to', 'have', 'been', 'distinguished', 'by', 'some', 'token', 'of', 'providential', 'agency', ';', 'and', 'in', 'the', 'important', 'revolution', 'just', 'accomplished', 'in', 'the', 'system', 'of', 'their', 'united', 'government', 'the', 'tranquil', 'deliberations', 'and', 'voluntary', 'consent', 'of', 'so', 'many', 'distinct', 'communities', 'from', 'which', 'the', 'event', 'has', 'resulted', 'can', 'not', 'be', 'compared', 'with', 'the', 'means', 'by', 'which', 'most']
>>> text_lov = [lovins_stem for word in text]
>>> print("Lovins stemmer: ", ' '.join(text_lov))

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("Lovins stemmer: ", ' '.join(text_lov))
TypeError: sequence item 0: expected string, function found
>>> text_lov
[<function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>, <function lovins_stem at 0x00000000041DA4A8>]
>>> lovins_stem("bitter")
'bitter'
>>> text_lov = [lovins_stem(word) for word in text]
>>> text_lov
['citizen', 'at', 'larg', 'les', 'than', 'either', '.', 'No', 'peopl', 'can', 'be', 'bound', 'to', 'acknowledg', 'and', 'ador', 'th', 'Invis', 'Hand', 'which', 'conduc', 'th', 'affair', 'of', 'men', 'mor', 'than', 'thos', 'of', 'th', 'Unit', 'St', '.', 'Ev', 'step', 'by', 'which', 'the', 'hav', 'adv', 'to', 'th', 'character', 'of', 'an', 'indepens', 'nat', 'seem', 'to', 'hav', 'been', 'distingu', 'by', 'som', 'tok', 'of', 'provid', 'ag', ';', 'and', 'in', 'th', 'import', 'revolut', 'just', 'accompl', 'in', 'th', 'system', 'of', 'their', 'unit', 'governm', 'th', 'tranquil', 'deliber', 'and', 'volunt', 'cons', 'of', 'so', 'man', 'distinct', 'commun', 'from', 'which', 'th', 'evens', 'ha', 'result', 'can', 'not', 'be', 'compar', 'with', 'th', 'mean', 'by', 'which', 'most']
>>> Lovins_MVC = 1.0*len(set(text))/len(set(text_lov))
>>> Lovins_MVC
1.0
>>> #Lovins_ICF = 0
>>> lovins_stem("thieves")
'thief'
>>> scipy

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    scipy
NameError: name 'scipy' is not defined
>>> import scipy

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    import scipy
ImportError: No module named scipy
>>> def hamming2(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

>>> hamming2("hello", "hell")

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    hamming2("hello", "hell")
  File "<pyshell#19>", line 2, in hamming2
    assert len(s1) == len(s2)
AssertionError
>>> hamming2("hello", "hellp")
1
>>> define MHD:
	
SyntaxError: invalid syntax
>>> def MHD:
	
SyntaxError: invalid syntax
>>> def MHD(s1, s2):
	return hamming2)
SyntaxError: invalid syntax
>>> def MHD(s1, s2):
	p = min(len(s1), len(s2))
	q = max(len(s1), len(s2))
	return hamming2(s1[:p], s2[:p]) + q - p

>>> MHD("hello", "hell")
1
>>> MHD("helping", "hell")
4
>>> MHD("party", "parties")
3
>>> 

>>> 
>>> MHD_lovins = [MHD(i,j) for (i,j) in zip(text, text_lov)]
>>> MHD_lovins
[1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 4, 0, 0, 2, 1, 1, 0, 0, 1, 0, 1, 0, 1, 2, 4, 0, 3, 0, 0, 0, 1, 1, 5, 0, 1, 0, 0, 0, 4, 3, 1, 0, 1, 0, 5, 0, 1, 2, 0, 6, 4, 0, 0, 0, 1, 3, 3, 0, 5, 0, 1, 0, 0, 0, 2, 3, 1, 0, 6, 0, 3, 3, 0, 0, 1, 0, 5, 0, 0, 1, 1, 1, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0]
>>> 
>>> 
