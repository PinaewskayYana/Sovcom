import psycopg2
from collections import defaultdict
user = defaultdict()

con = psycopg2.connect(
  database="SovDB", 
  user="postgres", 
  password="password", 
  host="127.0.0.1", 
  port="5432"
)
