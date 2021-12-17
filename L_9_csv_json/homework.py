import csv

with open('2019.csv', 'r', encoding='utf8') as csv_file:
    reader = csv.DictReader(csv_file)
    highest = sorted(reader, key=lambda x: x['GDP per capita'])[-10:]
    print(highest)