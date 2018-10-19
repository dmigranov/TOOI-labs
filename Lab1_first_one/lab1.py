import csv


def areSimilar(row1, row2):
    for i in range(0, min(len(row1), len(row2))):
        if row1[i] == row2[i]:
            return True;
    return False;


with open('1.csv', 'r') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=',', quotechar='"')
    for row1 in csvreader1:
        with open('1.csv', 'r') as csvfile2:
            csvreader2 = csv.reader(csvfile2, delimiter=',', quotechar='"')
            for row2 in csvreader2:
                if areSimilar(row1, row2) and row1 != row2:
                    print(', '.join(row1))
                    print(', '.join(row2))
                    print
                


            
        



