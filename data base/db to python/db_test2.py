import sqlite3

conn=sqlite3.connect("db/teste.db")

cur=conn.cursor()


it_produtos_sql="insert into Productos Values ('Caneta',3,2.5)"


cur.execute(it_produtos_sql)
conn.commit()
conn.close