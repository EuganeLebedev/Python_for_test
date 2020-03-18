import csv
from pprint import pprint

with open('test3.csv') as f:
    reader = csv.DictReader(f, fieldnames=['MyCil1','MyCol2', 'MyCol3', 'MyCol4'])

    for rows in reader:
        pprint(row)
