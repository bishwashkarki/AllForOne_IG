import sqlite3
from sqlite3.dbapi2 import connect

conn=sqlite3.connect("db\loja.db")

cur=conn.cursor()
decl_sql="CREATE TABLE IF NOT EXISTS Productos(produto TEXT, quantidade INTEGER, preco REAL)"

cur.execute(decl_sql)
conn.commit()
conn.close