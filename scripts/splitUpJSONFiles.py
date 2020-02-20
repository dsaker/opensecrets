import os

congress = ['113', '114', '115', '116']
billType = ['hconres', 'hjres', 'hr', 'hres', 's', 'sconres', 'sjres', 'sres']

for con in congress:
    for bill in billType:
        os.mkdir("../data/JSON/text/" + con + "/" + bill)