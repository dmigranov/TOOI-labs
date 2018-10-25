import csv

with open('stage3_test.csv', 'r', encoding = 'utf-8') as source, open('mt3.csv', 'w', encoding = 'utf-8') as dest1, open('price.csv', 'w', encoding = 'utf-8') as dest2, open('cols.csv', 'w', encoding = 'utf-8') as dest3:
    reader = csv.DictReader(source)
    writer1 = csv.DictWriter(dest1, fieldnames = reader.fieldnames)
    writer2 = csv.DictWriter(dest2, fieldnames = reader.fieldnames)
    writer3 = csv.DictWriter(dest3, fieldnames = [reader.fieldnames[0], reader.fieldnames[2], reader.fieldnames[4]])
    #writer.writerow(reader.fieldnames)
    writer1.writeheader()
    writer2.writeheader()
    for row in reader:
        #print(row['Images'].count(',') + 1)
        if row['Images'].count(',') + 1 > 3:
            writer1.writerow(row)
        if float(row['Price']) > 10000 and float(row['Price']) <= 50000:
            writer2.writerow(row)
        newrow = {'Id' : row['Id'], 'Title' : row['Title'], 'Price' : row['Price']}
        writer3.writerow(newrow)
