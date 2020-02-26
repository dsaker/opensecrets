import requests
from bs4 import BeautifulSoup as BS
import json

last = {'2009': 220, '2011': 246, '2013': 213, '2015': 242, '2017': 272, '2019' : 219}

def add_bills(bills, rows):
    for row in rows:
        bill = {}
        data = row.findAll('td')
        bill['href']= data[1].find('a').get('href')
        bill['bill_id'] = data[1].text
        bill['status'] = data[2].text
        bill['title'] = data[3].text.split(' - ')[0]
    bills.append(bill)

for year in range(2009, 2020, 2):
    bills = []
    url = "https://legiscan.com/US/legislation/"+str(year)
    response = requests.get(url)
    soup = BS(response.text, features="html.parser")
    rows = soup.find('table').find('tbody').findAll('tr')
    add_bills(bills, rows)
    last_page = last[str(year)]
    for i in range(1, last_page):
        url = "https://legiscan.com/US/legislation/"+str(year)+"?page="+str(i)
        response = requests.get(url)
        soup = BS(response.text, features="html.parser")
        rows = soup.find('table').find('tbody').findAll('tr')
        add_bills(bills, rows)
        print(i)

    with open('../data/LegisScanData/'+str(year)+'links.json', 'w') as outfile:
        json.dump(bills, outfile)