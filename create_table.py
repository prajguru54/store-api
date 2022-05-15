import sqlite3

#Make connection
connection = sqlite3.connect('db_store.db')
cursor = connection.cursor()

#Create users table
create_table_query = 'CREATE TABLE IF NOT EXISTS USERS(ID INTEGER PRIMARY KEY, USERNAME TEXT, PASSWORD TEXT)'
cursor.execute(create_table_query)

#Create items table
create_table_query = 'CREATE TABLE IF NOT EXISTS ITEMS(ID INTEGER PRIMARY KEY, NAME TEXT, PRICE REAL)'
cursor.execute(create_table_query)

# cursor.execute("insert into items values(1,'banana', 20)")
# cursor.execute("insert into items values('apple', 120)")

#Insert 
# insert_query = 'INSERT INTO USERS VALUES(?, ?, ?)'
# users = [(1, 'Sribastav', '123'), (2, 'Jou', '456')]
# cursor.executemany(insert_query,users )

connection.commit()
connection.close()