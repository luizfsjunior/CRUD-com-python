import sqlite3 as lite

con = lite.connect('Banco.db')


def inserir(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO formulario (título, descrição, quantidade_series, quatidade_rep) VALUES (?, ?, ?, ?)'
        cur.execute(query,i)

def mostrar_info():
    lista_info = []
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM formulario'
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista_info.append(i)
    return lista_info


def update(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE formulario SET título=?, descrição=?, quantidade_series =?, quatidade_rep=? WHERE cod_exercicio=?'
        cur.execute(query,i)

def delete(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM formulario WHERE cod_exercicio=?'
        cur.execute(query,i)