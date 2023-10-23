import psycopg2
from collections import defaultdict
import random
appl_num = random.randrange(10000000)
user = defaultdict()
con = psycopg2.connect(
  database="SovDB", 
  user="postgres", 
  password="password", 
  host="127.0.0.1", 
  port="5432"
)
cur = con.cursor()
cur.execute(
    f"""SELECT idr, category, description, mincount from req WHERE category = 'Транспорт'"""
        )
req_tc = cur.fetchall()
con.commit()
con.close()

con = psycopg2.connect(
  database="SovDB", 
  user="postgres", 
  password="password", 
  host="127.0.0.1", 
  port="5432"
)
cur = con.cursor()
cur.execute(
    f"""SELECT idr, category, description, mincount from req WHERE category = 'Недвижимость'"""
        )
req_ne = cur.fetchall()
con.close()

con = psycopg2.connect(
  database="SovDB", 
  user="postgres", 
  password="password", 
  host="127.0.0.1", 
  port="5432"
)
cur = con.cursor()
cur.execute(
    f"""SELECT ida, cath, usid, text, status from application WHERE status = 'отправлена'"""
        )

aplicat_admin = cur.fetchall()
con.commit()
con.close()

con = psycopg2.connect(
  database="SovDB", 
  user="postgres", 
  password="password", 
  host="127.0.0.1", 
  port="5432"
)
cur = con.cursor()
cur.execute(
    f"""SELECT ida, cath, usid, text, status from application WHERE status = 'на корректировке'"""
        )

apl_cor = cur.fetchall()
con.commit()
con.close()
count_ph = 0
id_ap = 0
id_photo = ''
file_path = ''
next_state = ''
req_text = ''
id_req = 0
flag_plan = 0
id_client = 0