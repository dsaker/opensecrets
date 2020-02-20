import json
import csv
import os 

headers = ['bill_id', 'text']
congress = ['113', '114', '115', '116']

for con in congress:
    directory = "../../data/BILLSJSON/BILLStext/" + con
    for filename in os.listdir(directory):
        with open(directory + '/' + filename, encoding='utf-8', mode='r') as jf:
            dj = json.load(jf)
        csv_file = open("../../data/BILLSCSV/"+con+"/"+filename[:-4]+"csv", 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)
        for row in dj:
            csv_writer.writerow((row['bill_id'], row['text']))
        csv_file.close()