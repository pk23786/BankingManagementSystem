import cx_Oracle

class DB_Connection:
    ''' Make a connection with the database'''
    con = cx_Oracle.connect("SYSTEM/Qwerty@123@localhost:1521/orcl")
    cur = con.cursor()