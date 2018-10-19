import csv
import itertools
import operator


def areSimilar(row1, row2):
    for i in range(0, min(len(row1), len(row2))):
        if row1[i] == row2[i]:
            return True;
    return False;


with open('1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    sortedlist = sorted(csvreader, key = operator.itemgetter(0), reverse = True)
    data = [row for row in sortedlist]

for row in sortedlist:
    print row


        
                


            
        



