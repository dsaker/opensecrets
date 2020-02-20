import os
import json

congress = ['113', '114', '115', '116']
billType = ['hconres', 'hjres', 'hr', 'hres', 's', 'sconres', 'sjres', 'sres']

for con in congress:
    #print(con)
    hconres = []
    hjres = []
    hr = []
    hres = []
    s = []
    sconres = []
    sjres = []
    sres = []
    missed = []
    filename = '../../data/BILLSJSON/BILLStext/' + con + 'TextOnly.json'
    with open(filename, 'r') as json_file:
        json_object = json.load(json_file)
        for row in json_object:
            if row['bill_id'].startswith("BILLS-"+con+"hjres"):
                hjres.append(row)
            elif row['bill_id'].startswith("BILLS-"+con+"hconres"):
                hconres.append(row)
            elif row['bill_id'].startswith("BILLS-"+con+"hres"):
                hres.append(row)
            elif row['bill_id'].startswith("BILLS-"+con+"sconres"):
                sconres.append(row)
            elif row['bill_id'].startswith("BILLS-"+con+"sjres"):
                sjres.append(row)
            elif row['bill_id'].startswith("BILLS-"+con+"sres"):
                sres.append(row)
            elif row['bill_id'].startswith("BILLS-"+con+"hr"):
                hr.append(row)
            elif row['bill_id'].startswith("BILLS-"+con+"s"):
                            s.append(row)
            else:
                missed.append(row)
        with open("../../data/BILLSJSON/BILLStext/"+con+"/hconres.json", 'w') as f:
            json.dump(hconres, f, indent=4)
        with open("../../data/BILLSJSON/BILLStext/"+con+"/hjres.json", 'w') as f:
            json.dump(hjres, f, indent=4)
        with open("../../data/BILLSJSON/BILLStext/"+con+"/hr.json", 'w') as f:
            json.dump(hr, f, indent=4)
        with open("../../data/BILLSJSON/BILLStext/"+con+"/hres.json", 'w') as f:
            json.dump(hres, f, indent=4)
        with open("../../data/BILLSJSON/BILLStext/"+con+"/s.json", 'w') as f:
            json.dump(s, f, indent=4)
        with open("../../data/BILLSJSON/BILLStext/"+con+"/sconres.json", 'w') as f:
            json.dump(sconres, f, indent=4)
        with open("../../data/BILLSJSON/BILLStext/"+con+"/sjres.json", 'w') as f:
            json.dump(sjres, f, indent=4)
        with open("../../data/BILLSJSON/BILLStext/"+con+"/sres.json", 'w') as f:
            json.dump(sres, f, indent=4)
        with open("../../data/BILLSJSON/BILLStext/"+con+"/missed.json", 'w') as f:
            json.dump(missed, f, indent=4)
