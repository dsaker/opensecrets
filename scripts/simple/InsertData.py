import psycopg2

conn = psycopg2.connect("host=localhost dbname=opensecrets user=postgres password=postgres")
cur = conn.cursor()

with open("../../data/CampaignFinanceData/CFD1992/cands92.txt", 'r') as f:
    cur.copy_from(f, 'candidates', sep=',')
    conn.commit()


