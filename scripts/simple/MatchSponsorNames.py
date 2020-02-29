import json
import csv
import pickle
import pandas as pd

rev_dict_dubs = {'/US/people/mike-j-rogers/id/9382':'N00009668', '/US/people/mike-d-rogers/id/9220':'N00024759',
                '/US/people/donald-payne/id/9105':'N00000716', '/US/people/donald-payne-jr/id/14071':'N00034639'}

cfd_dubs = {'John Carter (R)':'N00025095', 'John Lewis (D)':'N00002577', 'Patrick Kennedy (D)':'N00000360', 'Jeff Miller (R)':'N00013846',
        'Connie Mack (R)':'N00026425', 'John Campbell (R)':'N00027565', 'Michael Fitzpatrick (R)':'N00027229', 'Duncan Hunter (R)':
        'N00029258', 'James McGovern (D)':'N00000179', 'Jim Banks (R)':'N00037185'}

wrong_name = {'Christopher Carney (D)': 'N00027703', 'Peter King (R)': 'N00001193', 'Benjamin Cardin (D)': 'N00001955', 'Lisa Murkowski (R)': 'N00026050', 'Christopher Dodd (D)': 'N00000581', 'Bernard Sanders (I)': 'N00000528', 'Edward Markey (D)': 'N00000270', 'Lacy Clay (D)': 'N00012460', 'Donna Christensen (D)': 'N00000133', 'Thomas Rooney (R)': 'N00029018', 'Michael Arcuri (D)': 'N00027890', 'Steven LaTourette (R)': 'N00003545', 'Thomas Carper (D)': 'N00012508', 'Richard Durbin (D)': 'N00004981', 'Edward Kaufman (D)': 'N00030767', 'Russell Feingold (D)': 'N00000036', 'Charles Dent (R)': 'N00026171', 'Michael Doyle (D)': 'N00001373', 'Thaddeus McCotter (R)': 'N00013808', 'Charles Gonzalez (D)': 'N00005960', 'G. Butterfield (D)': 'N00027035', 'Joe Baca (D)': 'N00007089', 'Parker Griffith (R)': 'N00029917', 'Thomas Perriello (D)': 'N00029339', 'Joseph Lieberman (I)': 'N00000616', 'Gerald Connolly (D)': 'N00029891', 'Sheila Jackson-Lee (D)': 'N00005818', 'Anh Cao (R)': 'N00030339', 'Henry Johnson (D)': 'N00027848', 'Michael Conaway (R)': 'N00026041', 'Michael Honda (D)': 'N00012611', 'James Himes (D)': 'N00029070', 'James Sensenbrenner (R)': 'N00004291', 'Thomas Petri (R)': 'N00004426', 'William Keating (D)': 'N00031933', 'Christopher Coons (D)': 'N00031820', 'Christopher Murphy (D)': 'N00027566', 'Jeffrey Landry (R)': 'N00031503', 'Fortney Stark (D)': 'N00007397', 'Stevan Pearce (R)': 'N00012672', 'James Moran (D)': 'N00002083', 'Robert Schilling (R)': 'N00030668', 'Howard McKeon (R)': 'N00006882', 'Debbie Stabenow (D)': 'N00004118', 'Pedro Pierluisi (N)': 'N00029168', 'Michael Enzi (R)': 'N00006249', 'Scott DesJarlais (R)': 'N00030957', 'Vern Buchanan (R)': 'N00027626', 'David Reichert (R)': 'N00026885', 'Theodore Deutch (D)': 'N00031317', 'John Rockefeller (D)': 'N00001685', 'Francisco Canseco (R)': 'N00026722', 'Daniel Coats (R)': 'N00003845', 'Christopher Smith (R)': 'N00009816', 'Jim DeMint (R)': 'N00002472', 'Harold Rogers (R)': 'N00003473', 'Krysten Sinema (D)': 'N00033983', 'Richard Nolan (D)': 'N00021207', 'Matthew Cartwright (D)': 'N00034128', 'Daniel Kildee (D)': 'N00033395', 'Eric Crawford (R)': 'N00030770', 'Edward Royce (R)': 'N00008264', 'Jim Bridenstine (R)': 'N00033532', 'Janice Schakowsky (D)': 'N00004724', 'Christopher Gibson (R)': 'N00031998', 'David Roe (R)': 'N00028463', 'Louie Gohmert (R)': 'N00026148', 'Charles Fleischmann (R)': 'N00030815', 'Patrick Tiberi (R)': 'N00009699', 'Timothy Walz (D)': 'N00027467', 'Garland Barr (R)': 'N00031233', 'Donald Norcross (D)': 'N00036154', 'James Langevin (D)': 'N00009724', 'Joseph Heck (R)': 'N00031244', 'Doug Lamborn (R)': 'N00028133', 'James Renacci (R)': 'N00031127', 'Alexander Mooney (R)': 'N00033814', 'Joseph Pitts (R)': 'N00001633', 'Steve Russell (R)': 'N00036175', 'Robert Wittman (R)': 'N00029459', 'Margaret Hassan (D)': 'N00038397', 'Thomas Garrett (R)': 'N00038847', 'Earl Carter (R)': 'N00035346', 'Luis Correa (D)': 'N00037260', 'Jody Arrington (R)': 'N00038285', 'Charlie Crist (D)': 'N00002942', 'Stephen Knight (R)': 'N00035820', 'Jack Bergman (R)': 'N00039533', 'C.A. Ruppersberger (D)': 'N00025482', 'Bradley Schneider (D)': 'N00033101', 'Jenniffer Gonzalez-Colon (R)': 'N00037615', 'Mark DeSaulnier (D)': 'N00030709', 'David Trott (R)': 'N00035607', 'Ed Perlmutter (D)': 'N00027510', 'Joseph Kennedy (D)': 'N00034044', 'Will Hurd (R)': 'N00031417', 'Michael Simpson (R)': 'N00006263', 'Debbie Lesko (D)': 'N00042056', 'Christopher Pappas (D)': 'N00042161', 'Elizabeth Fletcher (D)': 'N00041194', 'Steve Daines (R)': 'N00033054', 'Amata Radewagen (D)': 'N00007635', 'Thomas Suozzi (D)': 'N00038742', 'Al Lawson (D)': 'N00030642', 'Suzanne Lee (D)': 'N00037247', 'Kelly Loeffler (R)': 'NULL', 'Gregory Pence (R)': 'N00041956'}


fields = ['cid', 'nameParty', 'fullname', 'othername', 'party', 'state', 'href']

df = pd.read_csv('../../CampaignFinanceData/CFDCandShortNames08-18.csv')
df = df.set_index('cid')

sponsors_added = {'0'}
new_rows = []
for year in range(2009, 2020, 2):
    print(year)
    with open('CidSponsor'+ str(year) +'.json', 'r') as jf:
        jo = json.load(jf)
        for row in jo:
            for s in row['sponsors']:
                cid = s['CFDid']
                if cid not in sponsors_added:
                    if cid != 'NULL':
                        other_name = df.loc[cid].firstlastp[:-4]
                    else:
                        other_name = s["fullname"]
                    new_rows.append([cid, s["nameParty"], s["fullname"], other_name, s["party"], s["state"], s["href"]])
                    sponsors_added.add(cid)

with open('csv/CidSponsorFull.csv', 'w') as wf:
    csvwriter = csv.writer(wf)
    csvwriter.writerow(fields) 
    csvwriter.writerows(new_rows)
'''

df = pd.read_csv('../../CampaignFinanceData/CFDCandShortNames08-18.csv')
df = df.set_index('shortname')
print(df.head())
#duplicates = df[df.duplicated(subset = 'shortname', keep=False)]
#duplicates = duplicates.sort_values('shortname')
#duplicate_set = set(duplicates['shortname'])

for year in range(2009, 2020, 2):
    print(year)
    new_rows = []
    with open(str(year) + 'SponsorsCid.json', 'r') as jf:
        jo = json.load(jf)
        for row in jo:
            for s in row['sponsors']:
                nameParty = s['nameParty']
                link = s['href']
                if rev_dict_dubs.get(link):
                    s['CFDid'] = rev_dict_dubs[link]
                elif wrong_name.get(nameParty):
                    s['CFDid'] = wrong_name[nameParty]
                elif cfd_dubs.get(nameParty):
                    s['CFDid'] = cfd_dubs[nameParty]
                else:
                    s['CFDid'] = df.loc[nameParty].cid
            new_rows.append(row)

    with open('CidSponsor' + str(year) + '.json', 'w') as wf:
        json.dump(new_rows, wf, indent=4)


rev_dict = {} 
for key, value in sponsor_links.items(): 
    rev_dict.setdefault(value, set()).add(key) 
  
result = filter(lambda x: len(x)>1, rev_dict.values())


for year in range(2009, 2020, 2):
    filename = str(year) + 'SponsorsSubjects.json'
    with open(filename, 'r') as jf:
        jo = json.load(jf)
        count = 0
        for row in jo:
            if count > 3:
                break
            print(row['bill_id'])
            for sponsor in row['sponsors']:
                fullnameParty = sponsor['first'] + ' ' + sponsor['last'] + ' (' + sponsor['party'] + ')'
                if fullnameParty not in uniqueSponsors:
                    uniqueSponsors.append(fullnameParty)

with open('../../CampaignFinanceData/CFDCandNamesCycle.csv', 'r') as cf, open('../../CFDCandShortNames08-18.csv', 'w') as wo:
    reader = csv.reader(cf)
    writer = csv.writer(wo)
    for row in reader:
        print(row)
        if len(row[2].split(" ")) > 3:
            namelist = row[2].split(' ')
            if namelist[-2] in ['Jr', 'Jr.', 'I', 'II', 'III']:
                lastname = namelist[-3]
            else: 
                lastname = namelist[-2]
            row.append(namelist[0] + ' ' + lastname + ' ' + namelist[-1])
        else:
            row.append(row[2])
        writer.writerow(row)'''