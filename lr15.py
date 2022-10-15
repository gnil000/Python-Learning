import sqlite3

con = sqlite3.connect('newDB.db')
cursorObj = con.cursor()


con.close()
