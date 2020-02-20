import json
import csv

headers = ['bill_id', 'text']

with open("../../data/BILLSJSON/BILLStext/113/hconres.json", encoding='utf-8', mode='r') as jf:
    dj = json.load(jf)

csv_file = open("../../data/BILLSJSON/BILLStext/113/hconres.csv", 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(headers)

for row in dj:
    csv_writer.writerow((row['bill_id'], row['text']))

csv_file.close()