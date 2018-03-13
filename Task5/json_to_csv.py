# Parse .json file format to .csv file format


import json
import csv

data = open('data.json').read()
rows = json.loads(data)
row = rows.values()

with open('convert.csv', 'w') as file:
    cwriter = csv.writer(file)
    cwriter.writerow(rows)
    cwriter.writerow(row)