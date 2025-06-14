import sqlite3

conn = sqlite3.connect('practice.db')

# execute SQL statements and fetch results from SQL queries using Cursor 
cursor = conn.cursor()

# Create table in database using CREATE statement
cursor.execute(''' CREATE TABLE IF NOT EXISTS movie(title, year, score) ''')

result = cursor.execute("SELECT name FROM sqlite_master")
print(result.fetchone())        # tables are stored in a form of tuples in python sqlite

# Insert value into table movie
cursor.execute(''' INSERT INTO movie VALUES 
               ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5) 
''')
conn.commit()           # Commit database operations

result = cursor.execute("SELECT * FROM movie")
save = result.fetchall() 
print(save)