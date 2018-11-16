import collections



#1.1
import xml.etree.ElementTree as etree
tree = etree.parse('file.xml')
root = tree.getroot()
cnt = collections.Counter()

for source in root.iter('source'):
    l = source.text.split()
    for word in l:
        cnt[word] += 1 #word.lower()

print(cnt.most_common(10))
