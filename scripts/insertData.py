import psycopg2

conn = psycopg2.connect("host=localhost dbname=OpenSecretsDB user=postgres password=nov261979")
cur = conn.cursor()
with open("cands90.csv", 'r') as f:
    cur.copy_from(f, 'candidates', sep=',')
    conn.commit()

