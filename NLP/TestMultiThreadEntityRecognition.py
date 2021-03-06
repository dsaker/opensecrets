import spacy 
import pandas
import re
import time
from threading import Thread


billType = ['hconres', 'hjres', 'hr', 'hres', 's', 'sconres', 'sjres', 'sres']

congress = ['113', '114', '115', '116']

stop_words = {'Whereas', 'The United States', 'the United States','Capitol', 'National', 'Congress', 'Government', 'Federal', 'House', 'Senate', \
    'The House of Representatives','section', 'Ther', 'South', 'the United States of America', 'Sec', 'TITLE', 'America', 'American', 'United States', \
    'State', 'Nation', 'Act'}

stop_entities = ['DATE', 'QUANTITY', 'CARDINAL', 'ORDINAL', 'PERCENT', 'TIME']

romanNumeral = re.compile('^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$')

spacy_nlp = spacy.load("en_core_web_sm") 

def find_entities(dataset, dname):
    entityArray = []

    if len(dataset) < 100:
        r = len(dataset)
    else: r = 100 
    
    for i in range(r):
        d = dataset['text'][i]
        if len(d) > 1000000:
            d = d[:1000000-1] 
        doc = spacy_nlp(d) 
        for ent in doc.ents:
            if ent.label_ not in stop_entities and ent.text not in stop_words and not romanNumeral.match(ent.text) \
                and 'section' not in ent.text: 
                entityArray.append((re.sub(' +', ' ', ent.text),  ent.label_))
    print(dname)
    print("length = %d" % (len(entityArray)))

start_time = time.time()

threads = []

for bill in billType:
    dataset = pandas.read_csv('../data/BILLSCSV/113/' + bill + ".csv")
    thread = Thread(target=find_entities, args=(dataset, bill))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print("time = ", end_time - start_time)