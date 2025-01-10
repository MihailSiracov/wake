import sqlite3
import datetime

con = sqlite3.connect("data.db", check_same_thread=False)
cursor = con.cursor()
cursor.execute(f"""CREATE TABLE IF NOT EXISTS time_table
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER, 
                hour INTEGER,
                minute INTEGER,
                weekday INTEGER)""")


def time_dt():
    time_now = datetime.datetime.now()
    year = time_now.year
    month = time_now.month
    day = time_now.day
    hour = time_now.hour
    minute = time_now.minute
    weekday = datetime.datetime.weekday(time_now)
    #cursor.execute(f"SELECT COUNT * FROM time_table WHERE NOT  ")
    #return cursor.fetchall()

time_dt()


def into_table():
    print('jrgk')


def out_of_table():
    print("iughuefioj")

cursor.connection.commit()
cursor.close()