import psycopg2
import csv

conn = psycopg2.connect(database="d6nj4q304bh0i3", user="sdwoftdverxgtg",
                        password="e83401bbdd19760eb2fc2ed9a2f3c894e2e09fe3dd01f00e6bc1e4cd679d8b02",
                        host="ec2-34-197-141-7.compute-1.amazonaws.com",
                        port="5432")

print("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE reviews
      (title    TEXT    NOT NULL,
      isbn  varchar     NOT NULL,
      review varchar    NOT NULL,
      user_name varchar    NOT NULL
);''')
print("Table created successfully")


conn.commit()
conn.close()
