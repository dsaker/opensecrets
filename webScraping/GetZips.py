import requests
import json

with open('BILLSUMzips.json') as json_file:
    links = json.load(json_file)
    for link in links:
        print(link)
        response = requests.get(link, headers={'Accept': 'application/xhtml+xml,application/xml;q=0.9'})
        with open('../data/BILLSUM/ZIPS'+link.split('/')[7], 'wb') as f:
            f.write(response.content)