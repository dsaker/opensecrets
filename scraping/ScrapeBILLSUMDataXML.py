import requests
from xml.etree import ElementTree as ET
import json

congress = ['113', '114', '115', '116']
billType = ['hconres', 'hjres', 'hr', 'hres', 's', 'sconres', 'sjres', 'sres']

links = []

for year in congress:
    for btype in billType:
        response = requests.get("https://www.govinfo.gov/bulkdata/BILLSUM/"+year+"/"+btype,headers={'Accept': 'application/xhtml+xml,application/xml;q=0.9'})
        root = ET.fromstring(response.text)
        tree = ET.ElementTree(root)
        for child in root.iter('link'):
            if child.text[-3:] == 'zip':
                links.append(child.text)

with open('BILLSUMzips.json', 'w') as outfile:
    json.dump(links, outfile)


'''for child in root.iter('*'):
    print(child.tag)'''
