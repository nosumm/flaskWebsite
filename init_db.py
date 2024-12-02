import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Project 1', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Project 2', 'Content for the second post')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Project 3', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Project 4', 'Content for the second post')
            )

connection.commit()
connection.close()
