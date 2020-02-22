import json
import requests

with open('billsLinks.json') as json_file:
    links = json.load(json_file)
    for link in links:
        response = requests.get(link, headers={'Accept': 'application/xhtml+xml,application/xml;q=0.9'})
        with open('../data/BILLSUMS/'+link.split('/')[7], 'w') as f:
            f.write(response.text)