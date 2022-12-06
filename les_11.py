import sqlite3

conn = sqlite3.connect('homework.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS statuses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(10) UNIQUE);''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS categories(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(36) UNIQUE);''')

cur.execute('''
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
name VARCHAR(24),
email VARCHAR(24) UNIQUE);''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
status_id INTEGER, 
FOREIGN KEY (user_id) REFERENCES user(id),
FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE CASCADE
);
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(36),
descr VARCHAR(140),
category_id INTEGER,
FOREIGN KEY (category_id) REFERENCES categories(id));
''')
conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS order_items(
id INTEGER PRIMARY KEY AUTOINCREMENT,
order_id INTEGER,
product_id INTEGER,
FOREIGN KEY (order_id) REFERENCES orders(id),
FOREIGN KEY (product_id) REFERENCES products(id));''')
conn.commit()







# cur.execute(''' CREATE TABLE IF NOT EXISTS categories(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(32) NOT NULL UNIQUE,
# is_published BOOLEAN DEFAULT(false));''')
# conn.commit()
#
# cur.execute('''
# CREATE TABLE IF NOT EXISTS products(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(32) NOT NULL,
# descr VARCHAR(1024),
# price DECIMAL(7, 2) NOT NULL DEFAULT(0.0),
# category_id INTEGER NOT NULL,
# FOREIGN KEY (category_id) REFERENCES categories(id)
# ON DELETE CASCADE
# );''')
# conn.commit()
