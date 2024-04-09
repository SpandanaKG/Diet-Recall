import sqlite3

conn = sqlite3.connect('diet_db.db')
cursor = conn.cursor()
cursor.execute("""create table user(email TEXT PRIMARY KEY UNIQUE NOT NULL,
password TEXT NOT NULL,
height REAL,
weight REAL,
sex TEXT,
diettype TEXT,
dob TEXT,
activity TEXT )""")
conn.commit()
conn.close()


# conn = sqlite3.connect('diet_db.db')
# cursor = conn.cursor()
# cursor.execute("INSERT INTO user VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)",
#             (1,"d@gmail.com", "123", 5.8, 67, "Male", "Keto", "31-01-1992", "Light"))
# conn.commit()
# conn.close()