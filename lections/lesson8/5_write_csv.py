import csv

with open('result.csv', 'w') as f:
    writer = csv.writer(f)

    writer.writerow((1, 2, 3, 4))
    writer.writerow((5, 6, 7, 8))
