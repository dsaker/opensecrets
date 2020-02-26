import json
import requests
from bs4 import BeautifulSoup as BS
from multiprocessing import Process

bills = []

def parse_request(soup, bill_id):
    bill = {}
    print(bill_id)
    bill['bill_id'] = bill_id
    bill['bill_summary'] = soup.find("div", {"id": "bill-summary"}).text
    bill['bill_title'] = soup.find("div", {"id": "bill-title"}).text
    sponsor_data = soup.find("div", {"id": "gaits-summary-sponsor"}).table.tbody.tr.findAll('td')
    sponsors = []
    if sponsor_data:
        for d in sponsor_data:
            sponsor = {}
            _, first, *_, last = d.text.split(' ')
            sponsor['first'] = first
            last, state = last.split('\xa0')
            sponsor['last'] = last
            state = state.replace('[', '').replace(']', '')
            party, state = state.split('-')
            sponsor['party'] = party
            sponsor['state'] = state
            sponsors.append(sponsor)
    bill['sponsors'] = sponsors
    subjects = []
    if soup.find('h2', string='Subjects'):
        h2 = soup.find('h2', string='Subjects')
        subs = h2.find_next_sibling('div').findAll('a')
        for subject in subs:
            if subject.text != "":
                subjects.append(subject.text)
    bill['subjects'] = subjects
    bills.append(bill)

year = '200/9'
filename = year+'links.json'
links = []
with open(filename, 'r') as jf:
    json_object = json.load(jf)
    for row in json_object:
        links.append('https://legiscan.com' + row['href'])

for link in links:
    bill_id = link.split('/')[5]
    response = requests.get(link)
    soup = BS(response.text, features="html.parser")
    parse_request(soup, bill_id)

with open('SponsorsSubjects/'+year+'SponsorsSubjects.json', 'w') as jf:
    json.dump(bills, jf, indent=4)