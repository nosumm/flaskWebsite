import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Maui 2024', 'Proposal Trip - November 2024')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Guatemala 2024', 'Natrice 30th Birthday Trip - June 2024')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Grand Turk 2024', 'Our first cruise - March 2024')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Italy 2023', 'Italy in November/December!')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Mexico City 2023', 'Mexico City - August 2023')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Ireland 2023', 'Ireland - Febuary 2023')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Ireland and Malta 2022', 'Ireland and Malta - June and July 2022')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Tulum 2020', 'Tulum in December 2020!')
            )

connection.commit()
connection.close()
