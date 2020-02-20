from bs4 import BeautifulSoup as bs
import json
import os
import re

congress = ['113', '114', '115', '116']
textrows = []

'''def replaceUnicode(s):
    s = re.sub(u"(\u2018|\u2019)", "'", s)
    s = re.sub(u"(\u201c|\u201d)", '"', s)
    s = re.sub(u"(\u2014|\u2013|\u00ad)", '-', s)
    s = re.sub(u"(\u2002|\u2009)", ' ', s)


    s = s.replace('\u0144', "n").replace('\u00bd', '1/2')
    s = s.replace('\u00b0', "degrees ").replace('\u2032', "`").replace('\u00f1',  "n")#.replace('\u00ad', "-").replace('\u2002',  ' ').replace('\u00bd', '1/2')

    return s'''

for con in congress:
    filename = '../data/JSON/BILLS' + con + '.json'
    with open(filename, 'r') as json_file:
        json_object = json.load(json_file)
        for row in json_object:
            textrow = {}
            text = ''
            textrow['bill_id'] = row['bill_id']
            if 'whereas' in row:
                ws = row['whereas']
                for wa in ws:
                    text += wa
            if 'resolution_body' in row:
                text += row['resolution_body']
            if 'legis_body'in row:
                text += row['legis_body']
            textrow['text'] = text
            textrows.append(textrow)

    with open('BILLS'+ con + 'text.json', encoding='utf-8', mode='w') as jsonfile:
        json.dump(textrows, jsonfile, indent=4)