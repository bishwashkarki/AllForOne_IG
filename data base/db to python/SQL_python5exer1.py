import sqlite3
def ler_tabela_cantores() :
    conn=sqlite3.connect ('db/teste_data.db')
    cur=conn.cursor()
    decl_sql='select * from clientes'
    cur.execute (decl_sql)
    registos=cur.fetchall() #ler todos os registos
    conn.close()
    return registos # Retorna uma lista de tuplos em que cada tuplo é um registo

reg=ler_tabela_cantores ()
print ('------Tabela------')
print (reg)
print ('-------1° Registo------')
print (reg[0])
print ('---Primeiro Nome e Email do 5° registo----')
print (reg[4][1], reg[4][3])
print ('-------1° Registo------')
print (reg[0,4])