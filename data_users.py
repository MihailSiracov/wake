import sqlite3
import datetime


con = sqlite3.connect("data.db", check_same_thread=False)
cursor = con.cursor()
cursor.execute(f"""CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                password TEXT,
                col_of_records INTEGER)""")
def adding(name, password):
    cursor.execute(f"INSERT INTO users (name, password) VALUES (?, ?)" ,(name, password,))
    cursor.connection.commit()

def finding(name, pussword, aim):
    finding_name = """SELECT * FROM users WHERE name=(?)"""
    finding_pussword = """SELECT * FROM users WHERE password=(?)"""
    if aim == 'for_enter':
        result = ["", ""]
        cursor.execute(finding_name, (name,))
        if cursor.fetchall() == []:
            result[0] = "Неправильное имя"
        cursor.execute(finding_pussword, (pussword,))
        if cursor.fetchall() == []:
            result[1] = "Неправильный пороль"
    else:
        result = ["", ""]
        cursor.execute(finding_pussword, (pussword,))
        if cursor.fetchall() != []:
            result[1] = "Измените пороль"
            return result
        cursor.execute(finding_name, (name,))
        if cursor.fetchall() != []:
            result[0] = "Измените имя"
    return result
