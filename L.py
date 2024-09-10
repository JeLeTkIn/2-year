import sqlite3

try:
    conn = sqlite3.connect('school.db')
    print("Подключение успешно")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade REAL
        )
    ''')


except sqlite3.Error as p:
    print(f"Ошибка подключения или выполнения запроса: {p}")

c.execute('''
        INSERT INTO users (name, age, grade) VALUES (?, ?, ?)
    ''', ('Alice', 20, 3.8))
c.execute('''
        INSERT INTO users (name, age, grade) VALUES (?, ?, ?)
    ''', ('Bob', 21, 3.5))
c.execute('''
        INSERT INTO users (name, age, grade) VALUES (?, ?, ?)
    ''', ('Charlie', 22, 3.9))

conn.commit()
c.execute('SELECT * FROM users')
print(c.fetchall())

c.execute('''
    UPDATE users 
    SET grade = ?
    WHERE id = ?
''', (3.7, 2))

conn.commit()

c.execute('SELECT * FROM users')
print(c.fetchall())

c.execute('''
    DELETE FROM users
    WHERE id = ?
''', (3,))

conn.commit()
c.execute('SELECT * FROM users')
print(c.fetchall())

c.execute('SELECT * FROM users WHERE age > 20')
print(c.fetchall())

c.execute('''ALTER TABLE users
          ADD COLUMN email TEXT''')

conn.commit()

c.execute('''
    UPDATE users 
    SET grade = ?
    WHERE age > 20
''',(4.0,))

conn.commit()

c.execute('SELECT * FROM users')
print(c.fetchall())

if conn:
    conn.close()
    print("Соединение закрыто")