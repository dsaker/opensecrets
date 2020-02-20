from bs4 import BeautifulSoup as bs
import csv
import os

congress = ['113', '114', '115', '116']
fields = ['measure_id', 'congress', 'measure_type', 'orig_publish_date', 'originchamber', 'update_date', 'title', 'summary']
rows = []

for con in congress:
    directory = '../data/BILLSUM/' + con + '/'
    for filename in os.listdir(directory):
        with open(directory + filename, 'r') as xml_file:
            soup = bs(xml_file, 'lxml')
            item = soup.find('item')
            congress = item.get('congress')
            measure_id = item.get('measure-id') 
            measure_type = item.get('measure-type')
            orig_publish_date = item.get('orig-publish-date')
            originchamber = item.get('originchamber')
            update_date = item.get('update-date')
            title = item.find('title').text
            summary = item.find('summary-text').text[:-3]
            rows.append([measure_id, congress, measure_type, orig_publish_date, originchamber, update_date, title, summary])

with open('BILLSUMS.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)