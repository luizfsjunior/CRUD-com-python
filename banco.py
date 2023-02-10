import sqlite3 as lite

con = lite.connect('Banco.db')


#Tabela
def cria_tabela():
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS formulario(cod_exercicio INTEGER PRIMARY KEY AUTOINCREMENT, título TEXT, descrição TEXT, quantidade_series INTEGER, quatidade_rep INTEGER)")