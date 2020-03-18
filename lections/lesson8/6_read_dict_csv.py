import csv
from pprint import pprint


with open('test2.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        pprint(row)
