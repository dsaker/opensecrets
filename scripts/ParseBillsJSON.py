from bs4 import BeautifulSoup as bs
import json
import os

congress = ['113', '114', '115', '116']
fields = ['measure_id', 'congress', 'measure_type', 'orig_publish_date', 'originchamber', 'update_date', 'title', 'summary']
rows = []
row = {}
filename = '../data/BILLS/113/BILLS-113hconres8ih.xml'
with open(filename, 'r') as xml_file:
    bills_id = filename.split('/')[4].split('.')[0]
    print(bills_id)
    lastdigit = max([i for i in range(len(bills_id)) if bills_id[i].isdigit()])
    sumbills_id = bills_id[:lastdigit+1]
    print(sumbills_id)

'''
for con in congress:
    directory = '../data/BILLS/' + con + '/'
    for filename in os.listdir(directory):
        row = {}
        with open(directory + filename, 'r') as xml_file:
            soup = bs(xml_file, 'lxml')
            sponsor = soup.find('sponsor')
            row['sponsor_id'] = sponsor.get('name-id')
            row['sponsor'] = sponsor.text
            if soup.find('cosponsor'):
                cosponsors = soup.findAll('cosponsor')
                cos = []
                for co in cosponsors:
                    cos.append(co.get('name-id'))
                row['cosponsors'] = cos
            else:
                row['cosponsors'] = []
            if soup.find('whereas'):
                ws = soup.findAll('whereas')
                was = []
                for wa in ws:
                    was.append(wa.text.replace('\t', '').replace('\n', ''))
                row['whereas'] = was
            else:
                row['whereas'] = []
            committee = soup.find('committee-name')
            row['committee_id'] = committee.get('committee-id')
            row['committee'] = committee.text.replace('\t', '').replace('\n', '')
            row['legis_type'] = soup.find('legis-type').text
            resolution = soup.find('resolution-body')
            row['resolution_body'] = resolution.find('section').text.replace('\n', '').replace('\t', '')
            rows.append(row)

with open('BILLS.json', 'w') as jsonfile:
    json.dump(rows, jsonfile, indent=4)'''