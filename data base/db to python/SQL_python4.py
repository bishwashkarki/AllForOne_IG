import sqlite3
#Ligar à base de dados (se não existir cria-a)
ligarBd = sqlite3.connect ("db/Discoteca.db")
#Criar cursor
cursor=ligarBd.cursor ()
#Criar a tabela
cursor.execute ("""CREATE TABLE IF NOT EXISTS albums
(titulo text, artista text, dataLancamento text,
editora text, tipo text)
""")

#Inserir um registo
cursor.execute ("INSERT INTO albums VALUES ('The Black Album', 'Metallica', '12/9/1991', 'Elektra Records', 'MP3')")
# Inserção de múltiplos registos
albums = [('Load', 'Metallica', '7/9/1996', 'Sony Music Entertainment', 'CD'),
          ('Master of Puppets', 'Metallica', '2/1/1986', 'Elektra Records', 'CD'),
          ('Hangar 18', 'Megadeth','4/17/1999', 'Vertigo Records', 'MP3'),
          ('Reload', 'Metallica', '7/9/1997', 'Sony Music Entertainment','CD'),
          ('Magic', 'Queen', '7/9/1997', 'Sony Music Entertainment','CD')]
cursor.executemany ("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
#Inserção de dados a partir de um dicionário
data = {"titulo" : "Roots", "artista" : "Sepultura", "datalancamento":"29/11/2001", "editora":"Heavy Cage", "tipo":"Cassete"}
cursor.execute ("""
INSERT INTO albums (titulo, artista, datalancamento, editora, tipo)
VALUES (:titulo, :artista, :datalancamento, :editora, :tipo)""", data)

#Consulta de dados
print ("-------- Consulta de dados -------")
sql= "SELECT * FROM albums"
cursor.execute (sql)
consulta=cursor.fetchall() # ou usar fetchone (0 para apresentar o 1° registo
print (consulta)
    
#Consulta com ciclo for
print ("-------- Consulta de dados - ciclo for -------")
print ("\n ------- Lista de Albuns ------ \n") 
for row in cursor.execute ("SELECT * FROM albums"):
    print (row)

ligarBd.commit ()
ligarBd.close ()
print ("Gravação de dados finalizada!")                                                   
               