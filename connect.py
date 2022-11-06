import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="",
  host="local",
  port="5432"
)

print("Database opened successfully")