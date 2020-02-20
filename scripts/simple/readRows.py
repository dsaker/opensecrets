import json

labels = []

with open('../../data/BILLSJSON/BILLSComplete/BILLS113.json', 'r') as f:
    json_object = json.load(f)
    for row in json_object:
        
        last_digit = max([i for i in range()])
