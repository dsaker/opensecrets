import psycopg2

conn = psycopg2.connect("host=localhost dbname=opensecrets user=postgres password=postgres")
cur = conn.cursor()

for i in range(2010, 2019, 2):
    s = "../../data/CampaignFinanceData/CFD"+str(i)+"/csv/cands"+str(i)[2:]+".csv"
    print(s)
    with open(s, 'r') as f:
        cur.copy_from(f, 'candidates', sep=',')
        conn.commit()