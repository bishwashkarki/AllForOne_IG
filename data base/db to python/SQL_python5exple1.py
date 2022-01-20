import sqlite3
def ler_tabela_cantores() :
    conn=sqlite3.connect ('db/festival.db')
    cur=conn.cursor()
    decl_sql='select * from Cantores'
    cur.execute (decl_sql)
    registos=cur.fetchall() #ler todos os registos
    conn.close()
    return registos # Retorna uma lista de tuplos em que cada tuplo é um registo
reg=ler_tabela_cantores ()
print ('------Tabela------')
print (reg)
print ('-------1° Registo------')
print (reg[0])
print ('---Primeiro Nome e Tipo do 2° registo----')
print (reg[1][0], reg[1][3])
print ('------N°de registos------')
print (len(reg))


