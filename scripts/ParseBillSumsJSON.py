from bs4 import BeautifulSoup as bs
import json
import os

congress = ['113', '114', '115', '116']
fields = ['measure_id', 'congress', 'measure_type', 'orig_publish_date', 'originchamber', 'update_date', 'title', 'summary']
rows = []

for con in congress:
    directory = '../data/BILLSUM/' + con + '/'
    for filename in os.listdir(directory):
        row = {}
        with open(directory + filename, 'r') as xml_file:
            soup = bs(xml_file, 'lxml')
            item = soup.find('item')
            row['congress'] = item.get('congress')
            row['measure_id'] = item.get('measure-id') 
            row['measure_type'] = item.get('measure-type')
            row['orig_publish_date'] = item.get('orig-publish-date')
            row['originchamber'] = item.get('originchamber')
            row['update_date'] = item.get('update-date')
            row['title'] = item.find('title').text
            row['summary'] = item.find('summary-text').text[:-3]
            rows.append(row)

with open('BILLS.json', 'w') as jsonfile:
    json.dump(rows, jsonfile, indent=4)