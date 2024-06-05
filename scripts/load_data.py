import pandas as pd
import psycopg2
from datetime import datetime, timedelta

db_params = {
        'user': 'postgres',
        'password': 'thisistest1#',
        'host': 'database-1.c58ywwqk2w5e.us-east-2.rds.amazonaws.com',
        'port': '5432'
}

conn = psycopg2.connect(**db_params)
cur = conn.cursor()

df = pd.read_csv('driving_log.csv')

start_time = datetime.now()

for index, row in df.iterrows():
    timestamp = start_time + timedelta(seconds=index)
    cur.execute('''
    INSERT INTO telemetry_data (timestamp, steering, throttle, brake, speed)
    VALUES (%s, %s, %s, %s, %s)
    ''', (timestamp, row['steering'], row['throttle'], row['reverse'], row['speed']))
conn.commit()

cur.close()
conn.close()
