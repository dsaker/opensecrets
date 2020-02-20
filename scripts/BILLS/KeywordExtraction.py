import json
import csv

with open("../../data/BILLSJSON/BILLStext/113/hconres.json", encoding='utf-8', mode='r') as jf:
    dj = json.load(jf)

count = 0
for row in dj:
    if count > 5:
        break
    dataset = pd.read_json(row)
    print(dataset)
    count