import csv
import os 
import sys
import re

headers = ['bill_id', 'text']
congress = ['113', '114', '115', '116']

csv.field_size_limit(sys.maxsize)

new_rows = []

for con in congress:
    directory = "../../data/BILLSCSV/" + con
    for filename in os.listdir(directory):
        print(filename)
        with open(directory + '/' + filename, 'r') as cf:
            csvreader = csv.reader(cf) 
            fields = next(csvreader)
            new_rows.append(fields)
            for row in csvreader:
                text = row[1]
                if len(text) < 100:
                    continue
                else: 
                    text = text.replace("The", " The")
                    text = text.replace("This", " This")
                    text = text.replace("Section", " Section")
                    text = text.replace("Subsections", " Subsections")
                    text = text.replace("Paragraph", " Paragraph")
                    text = re.sub(' +', ' ', text)   
                new_rows.append([row[0], text])

        with open(directory + '/' + filename, 'w') as cfile: 
            
            csvwriter = csv.writer(cfile) 
            
            csvwriter.writerows(new_rows) 