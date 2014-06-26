
import csv


data = csv.reader(open('test_url.csv'))
fields = data.next() 
for row in data:
    item = dict(zip(fields, row))
    print item
