import sqlite3

CREATE_DEV = "CREATE TABLE devs(id INTEGER PRIMARY KEY, name TEXT, type TEXT, producent TEXT, serial_num TEXT PRIMARY KEY, dev_type TEXT);"

INSERT_DEV = "INSERT INTO devs(name, type, producent, serial_num, dev_type) VALUES (?, ?, ?, ?, ?);"

GET_ALL_DEVS = "SELECT * FROM devs;"
GET_DEVS_BY_SERIAL_NUM = "SELECT * FROM devs WHERE serial_num = ?;"
    

def connect(): 
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection: 
        connection.execute(CREATE_DEV)

def add_dev(connection, name, type, producent, serial_num, dev_type): 
    with connection: 
        connection.execute(INSERT_DEV, (name, type, producent, serial_num, dev_type))

def get_all_devs(connection): 
    with connection: 
        return connection.execute(GET_ALL_DEVS).fetchall()

def get_dev_by_serial_num(connection, serial_num): 
    with connection: 
        return connection.execute(GET_DEVS_BY_SERIAL_NUM, (serial_num,)).fetchall()