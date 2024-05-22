import psycopg2
import random
from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="example",
    host="db"
)
cursor = conn.cursor()