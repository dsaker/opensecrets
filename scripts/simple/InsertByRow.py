import psycopg2
import csv

conn = psycopg2.connect("host=localhost dbname=opensecrets user=postgres password=postgres")
cur = conn.cursor()

for i in range(2010, 2019, 2):
    s = "../../data/CampaignFinanceData/CFD"+str(i)+"/csv/cands"+str(i)[2:]+".csv"
    with open(s, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            cur.execute("INSERT INTO candidates VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
            conn.commit()
