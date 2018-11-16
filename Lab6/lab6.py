import collections



#1.1
import xml.etree.ElementTree as etree
tree = etree.parse('file.xml')
root = tree.getroot()
cnt = collections.Counter()
bicnt = collections.Counter()
order = collections.OrderedDict()


prev = ""
for token in root.iter('token'):
    flag = True
    biflag = True
    
    word = token.get("text")
    for g in token.iter('g'):
        if g.get('v') == "CONJ" or g.get('v') == "PREP" or g.get('v') == "PNCT" or g.get('v') == "UNKN":
            flag = False
        if g.get('v') == "PNCT" or g.get('v') == "UNKN":
            biflag = False
        
    if flag:
        cnt[token.get("text")] += 1
    if prev != "" and biflag and prevbiflag:
        bigram = (prev, word)
        bicnt[bigram]+=1
            
    prev = word
    prevbiflag = biflag
            

lenorder = collections.OrderedDict(sorted(cnt.items(), key=lambda t: len(t[0]), reverse=True))
unorder = collections.OrderedDict(sorted(cnt.items(), key=lambda t: t[1], reverse=False))
unique =0
for k,v in unorder.items():
    if v == 1:
        unique+=1

print("#1")
print("Most common", cnt.most_common(20))
print("Least common", cnt.most_common()[-19:])
print("Longest", list(lenorder.items())[0])
print("Bigrams", bicnt.most_common(20))
print("Unique", unique)
print("Size", len(lenorder))




#1.2
import json

with open('RomeoAndJuliet.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

cnt = collections.Counter()
bicnt = collections.Counter()
order = collections.OrderedDict()

prev = ""
for act in data["acts"]:
    for scene in act["scenes"]:
        action = scene["action"]
        for charwords in action:
            words = charwords["says"]
            for reply in words:
                l = reply.split()
                for word in l:
                    cnt[word] += 1
                    if prev != "":
                        bigram = (prev, word)
                        bicnt[bigram]+=1
                    prev = word

lenorder = collections.OrderedDict(sorted(cnt.items(), key=lambda t: len(t[0]), reverse=True))
unorder = collections.OrderedDict(sorted(cnt.items(), key=lambda t: t[1], reverse=False))
unique =0
for k,v in unorder.items():
    if v == 1:
        unique+=1
        
print("#2")
print("Most common", cnt.most_common(20))
print("Least common", cnt.most_common()[-19:])
print("Longest", list(lenorder.items())[0])
print("Bigrams", bicnt.most_common(20))
print("Unique", unique)
print("Size", len(lenorder))



#1.3
import csv
cnt = collections.Counter()
bicnt = collections.Counter()
order = collections.OrderedDict()

prev = ""
with open('stage3_test.csv', 'r', encoding = 'utf-8') as source, open('sorted.csv', 'w', encoding = 'utf-8') as dest:
    reader = csv.DictReader(source)
    #writer = csv.DictWriter(dest, fieldnames = [reader.fieldnames[0], reader.fieldnames[2], reader.fieldnames[4]])
    
    for row in reader:
        words = row["Title"].split() + row["Description"].split()
        for word in words:
            cnt[word] += 1
            if prev != "":
                bigram = (prev, word)
                bicnt[bigram]+=1
            prev = word
        
    
    
    
lenorder = collections.OrderedDict(sorted(cnt.items(), key=lambda t: len(t[0]), reverse=True))
unorder = collections.OrderedDict(sorted(cnt.items(), key=lambda t: t[1], reverse=False))
unique =0
for k,v in unorder.items():
    if v == 1:
        unique+=1
        
print("#3")
print("Most common", cnt.most_common(20))
print("Least common", cnt.most_common()[-19:])
print("Longest", list(lenorder.items())[0])
print("Bigrams", bicnt.most_common(20))
print("Unique", unique)
print("Size", len(lenorder))







