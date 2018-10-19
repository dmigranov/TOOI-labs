from itertools import product

def areSimilar(row1, row2):
    for i in range(0, min(len(row1), len(row2))):
        if row1[i] == row2[i]:
            return True;
    return False;


with open("1.csv") as csvfile:
    rows = csvfile.read().split("\n")
    cart = product(rows,rows)
    for i,j in cart:
        if areSimilar(i, j):
            print i,'is similar to',j

