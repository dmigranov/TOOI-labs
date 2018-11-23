import xml.etree.ElementTree as etree


class TFIDF_calculator:
    def __init__(self, filename):
        self.__tree = etree.parse(filename)
        #self.__root = self.__tree.getroot()
        self.__documents = list()
        self.__getDocuments() #удалить

    def __getDocuments(self):
        root = self.__tree.getroot()
        for paragraphs in root.iter('paragraphs'):
            document = list()
            for token in paragraphs.iter('token'):
                flag = True
                word = token.get("text")
                for g in token.iter('g'):
                    if g.get('v') == "CONJ" or g.get('v') == "PREP" or g.get('v') == "PNCT" or g.get('v') == "UNKN":
                        flag = False
                if flag:
                    document.append(word.lower())
            self.__documents.append(document)
            for word in document:
                print(word)
            print()
                        





tfidf = TFIDF_calculator('file.xml')
