import csv

with open('test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        csv_line = ','.join(row)
        print(csv_line)
