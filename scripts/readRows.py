import json

t = 1
s = 1
t2 = 0
s2 = 0

with open('BILLS113.json', 'r') as f:
    json_object = json.load(f)
    for row in json_object:
        if not 'legis_body' in row and not 'resolution_body' in row:
            print(row['bills_id'])

'''        if(len(row['title']) > t):
            t2 = t
            t = len(row['title'])
            tmeasureid = row['measure_id']
        if(len(row['summary']) > s):
            s2 = s
            s = len(row['summary'])
            smeasureid = row['measure_id']

print("longest title = %d" % t)
print("longest summary = %d" % s)
print(tmeasureid)
print(smeasureid)
print("2nd longest title = %d" % t2)
print("2nd longest summary = %d" % s2)'''

'''
BILLSUM
longest title = 1127 (id113hres370)
longest summary = 425321 (id114hr2029)
2nd longest title = 797
2nd longest summary = 356215
'''