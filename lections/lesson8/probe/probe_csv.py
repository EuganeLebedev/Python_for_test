import csv


with open('../../../OITM.csv', encoding='utf-8') as oitm:
    csv_reader = csv.DictReader(oitm, delimiter=';')
    for row in csv_reader:
        print(row['ItemCode   '])