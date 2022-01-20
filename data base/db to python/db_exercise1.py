#import modules
import sqlite3
import tkinter 

conn=sqlite3.connect("db/exer1.db")
cur=conn.cursor()  
#functions
def criar_tabela_produtos():

    decl_sql="CREATE TABLE IF NOT EXISTS Produtos(Produto TEXT, quantidade INTEGER, preco REAL)"

    cur.execute(decl_sql)
    conn.commit()
criar_tabela_produtos()
def inserir_tabela_produtos(produto,quantidade,preco):  

    it_sql="insert into Produtos values(?,?,?)"

    cur.execute(it_sql,(produto,quantidade,preco))
    conn.commit()
inserir_tabela_produtos('lápis',5,2.8)

def ler_tabela_produtos():
    ler_sql="select * from produtos"
    cur.execute(ler_sql)
    linhas=cur.fetchall()
    conn.commit()
    return linhas
produtos=ler_tabela_produtos()
print(produtos)

product1=input("find=")
product2=input("change=")

def atualizar_tabela_produtos(opt1,opt2):
    sql='''UPDATE EMPLOYEE SET produto(?) WHERE produto=(?);'''
    cur.execute(sql(opt1,opt2))
    conn.commit()
atualizar_tabela_produtos(product2,product1)

product3=input("find=")

def apagar_tabela_produtos(opt1):
    sql = "DELETE FROM customers WHERE address = '?'"
    cur.execute(sql(opt1))
    conn.commit()

apagar_tabela_produtos(product3)

"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

#tkinter settings
#win=tkinter.Tk()
#win.title("SQL and Python")
#win.resizable(False, False)
#
#
## Height and Width of our app
#app_width = 250
#app_height = 250
##Height and Width of our screen
#screen_width = win.winfo_screenwidth()
#screen_height = win.winfo_screenheight()
#
#x = (screen_width / 2) - (app_width / 2)
#y = (screen_height /2 ) - (app_height / 2)
#
#win.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")


#buttons
#button1=tkinter.Button(win,text="criar_tabela_produtos",command=lambda: criar_tabela_produtos)
#button1.pack()
#
#button2=tkinter.Button(win,text="inserir_tabela_produtos",command=lambda: inserir_tabela_produtos("lapis",5,2.8))
#button2.pack()
#
#button3=tkinter.Button(win,text="ler_tabela_produtos",command= ler_tabela_produtos)
#button3.pack()
#



#produtos = ler_tabela_produtos()
#print(produtos)






#win.mainloop()