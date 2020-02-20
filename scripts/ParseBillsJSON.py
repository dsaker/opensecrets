from bs4 import BeautifulSoup as bs
import json
import os

congress = ['113']
fields = ['bill_id', 'billsum_id', 'action_date', 'sponsor', 'sponsor_id', 'committe_name', 'committee_id', 'cosponsor', 'aciton_date', 'legis_type', 'resolution_body', 'legis_body']
rows = []

for con in congress:
    print(con)
    directory = '../data/BILLSxml/' + con + '/'
    for filename in os.listdir(directory):
        row = {}
        #print(filename)
        with open(directory + filename, 'r') as xml_file:
            # bill_id is unique for BILLS
            billstring = filename.split('/')
            bill_id = billstring[len(billstring)-1].split('.')[0]
            row['bill_id'] = bill_id
            print(bill_id)
            lastdigit = max([i for i in range(len(bill_id)) if bill_id[i].isdigit()])
            # billsum_id matches unique id of BILLSUM
            row['billsum_id'] = bill_id[:lastdigit+1]
            #start scraping  xml file 
            soup = bs(xml_file, 'lxml')
            if soup.find('action-date'):
                row['action_date'] = soup.find('action-date').text.replace('\t', ' ').replace('\n', ' ')
            if soup.find('sponsor'):
                sponsor = soup.find('sponsor')
                row['sponsor_id'] = sponsor.get('name-id')
                row['sponsor'] = sponsor.text.replace('\t', ' ').replace('\n', ' ')
            if soup.find('committee-name'):
                committee = soup.find('committee-name')
                row['committee_id'] = committee.get('committee-id')
                row['committee_name'] = committee.text.replace('\t', ' ').replace('\n', ' ')
            if soup.find('cosponsor'):
                cosponsors = soup.findAll('cosponsor')
                cos = []
                for co in cosponsors:
                    cos.append(co.get('name-id'))
                row['cosponsors'] = cos
            if soup.find('whereas'):
                ws = soup.findAll('whereas')
                was = []
                for wa in ws:
                    if wa.get('changed') == 'deleted':
                        continue
                    else:
                        was.append(wa.text.replace('\t', ' ').replace('\n', ' '))
                row['whereas'] = was
            if soup.find('legis-type'):
                row['legis_type'] = soup.find('legis-type').text.replace('\t', ' ').replace('\n', ' ')
            if soup.find('resolution-body'):
                resolutions = soup.findAll('resolution-body')
                for res in resolutions:
                    if res.find('section'):
                        section = res.find('section')
                        if section.get('changed') == 'deleted':
                            continue
                        else:
                            row['resolution_body'] = section.text.replace('\n', ' ').replace('\t', ' ')
                    else:
                        row['resolution_body'] = res.text
            if soup.find('legis-body'):
                row['legis_body'] = soup.find('legis-body').text.replace('\n', ' ').replace('\t', ' ')
            rows.append(row)

    with open('BILLS'+ con + '.json', 'w') as jsonfile:
        json.dump(rows, jsonfile, indent=4)