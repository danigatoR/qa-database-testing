import sqlite3


connection = sqlite3.connect("database/shop.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    INSERT INTO customers (name, email, phone)
    VALUES ('Daniel', 'dani@example.com', '612345678')
""")

connection.commit()

connection.close()