import xml.etree.ElementTree as etree
tree = etree.parse('file.xml')
root = tree.getroot()
sentences = open('sentences.txt', 'wb')
pluralnouns = open('pluralnouns.txt', 'wb')
#for text in root:
    #for paragraphs in text.findall('paragraphs'):
        #for paragraph in paragraphs:
            #for sentence in paragraph:
                #for source in sentence.findall('source'):
                    #sentences.write((source.text + '\n').encode('utf-8'))


    

for source in root.iter('source'):
    sentences.write((source.text + '\n').encode('utf-8'))


mVerb = 0
mConj = 0


for token in root.iter('token'):
    isNoun = False;
    isPlur = False;
    for g in token.iter('g'):
        #print(g.get('v'))
        if(token.get('text').lower() == 'может'):
            if g.get('v') == 'CONJ':
                mConj += 1
            elif g.get('v') == 'VERB':
                mVerb += 1
        if g.get('v') == 'NOUN':
            isNoun = True
        elif g.get('v') == 'plur':
            isPlur = True
    if(isPlur and isNoun):
        #print(token.get('text'))
        pluralnouns.write((token.get('text') + '\n').encode('utf-8'))

print(mVerb)
print(mConj)
    
        
        

