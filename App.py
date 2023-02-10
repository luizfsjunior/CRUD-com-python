from tkinter import *
from tkinter import ttk, messagebox

from view import *


#Cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#59c0f3"  # azul claro
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#d3d3d3"   # cinza claro


#Janela
janela = Tk()
janela.title('')
janela.geometry("1035x720")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

frame_title = Frame(janela, width=426, height=100, relief='flat',background=co2)
frame_title.grid(row=0, column=0)

frame_form = Frame(janela, width=426, height=620, relief='flat',background=co1)
frame_form.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_view = Frame(janela, width=800, height=620, relief='flat',background=co1)
frame_view.grid(row=0, column=1, rowspan=2, padx=1, pady=1, sticky=NSEW)




label_title = Label(frame_title,text="Formulário", anchor=NW, font=('Ivy 25 bold'), fg=co1,bg=co2, relief='flat')
label_title.place(x=110,y=25)




#Inserir dados

def inserir_dados():
    titulo = e_titulo.get() 
    desc = e_desc.get() 
    serie = e_serie.get() 
    rep = e_rep.get() 

    lista = [titulo, desc, serie, rep]

    if titulo == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        inserir(lista)
        messagebox.showinfo('Sucesso', "Os dados foram inseridos com sucesso")
        e_titulo.delete(0,'end') 
        e_desc.delete(0,'end') 
        e_serie.delete(0,'end') 
        e_rep.delete(0,'end') 

    for widget in frame_view.winfo_children():
        widget.destroy()

    mostrar()


global tree

#Atualizar dados
def atualizar_dados():
    try:
        tree_dados = tree.focus()
        tree_dict = tree.item(tree_dados)
        tree_list = tree_dict['values']

        valor = tree_list[0]

        e_titulo.delete(0,'end') 
        e_desc.delete(0,'end') 
        e_serie.delete(0,'end') 
        e_rep.delete(0,'end') 

        e_titulo.insert(0,tree_list[1]) 
        e_desc.insert(0,tree_list[2]) 
        e_serie.insert(0,tree_list[3]) 
        e_rep.insert(0,tree_list[4]) 

    
        def atualizar():
            titulo = e_titulo.get() 
            desc = e_desc.get() 
            serie = e_serie.get() 
            rep = e_rep.get() 

            lista = [titulo, desc, serie, rep, valor]

            if titulo == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                update(lista)
                messagebox.showinfo('Sucesso', "Os dados foram atualizados com sucesso"+str(lista))
                
                e_titulo.delete(0,'end') 
                e_desc.delete(0,'end') 
                e_serie.delete(0,'end') 
                e_rep.delete(0,'end') 

                b_conf.destroy()

            for widget in frame_view.winfo_children():
                widget.destroy()

            mostrar()

        b_conf = Button(frame_form, command=atualizar, text="Confirmar", width=10, anchor=NW, font=('ivy 10 bold'), bg =co8, fg=co1, relief='raised')
        b_conf.place(x=155, y=585)

        
        
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


def deletar_dados():
    try:
        tree_dados = tree.focus()
        tree_dict = tree.item(tree_dados)
        tree_list = tree_dict['values']

        valor = [tree_list[0]]

        delete(valor)
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        for widget in frame_view.winfo_children():
                widget.destroy()
        mostrar()
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')
        
#Titulo
l_titulo = Label(frame_form,text="Título", anchor=NW, font=('Ivy 13 bold'), fg=co4,bg=co1, relief='flat')
l_titulo.place(x=10,y=130)
e_titulo = Entry(frame_form, width=65, justify='left', relief='solid')
e_titulo.place(x=15,y=160)

#Descrição
l_desc = Label(frame_form,text="Descrição", anchor=NW, font=('Ivy 13 bold'), fg=co4,bg=co1, relief='flat')
l_desc.place(x=10,y=190)
e_desc = Entry(frame_form, width=65, justify='left', relief='solid')
e_desc.place(x=15,y=220)

#Séries
l_serie = Label(frame_form,text="Quatidade de Séries", anchor=NW, font=('Ivy 13 bold'), fg=co4,bg=co1, relief='flat')
l_serie.place(x=10,y=250)
e_serie = Entry(frame_form, width=8, justify='left', relief='solid')
e_serie.place(x=15,y=280)

#Repetições
l_rep = Label(frame_form,text="Quatidade de Repetições", anchor=NW, font=('Ivy 13 bold'), fg=co4,bg=co1, relief='flat')
l_rep.place(x=10,y=310)
e_rep = Entry(frame_form, width=8, justify='left', relief='solid')
e_rep.place(x=15,y=340)


#Botões
b_inserir = Button(frame_form, command=inserir_dados, text="Inserir", width=10, anchor=NW, font=('ivy 10 bold'), bg =co6, fg=co1, relief='raised')
b_inserir.place(x=15, y=550)

b_atualizar = Button(frame_form,command=atualizar_dados, text="Atualizar", width=10, anchor=NW, font=('ivy 10 bold'), bg =co8, fg=co1, relief='raised')
b_atualizar.place(x=155, y=550)

b_excluir = Button(frame_form,command=deletar_dados, text="Excluir", width=10, anchor=NW, font=('ivy 10 bold'), bg =co7, fg=co1, relief='raised')
b_excluir.place(x=295, y=550)



#Frame_view

def mostrar():
    global tree
    lista = mostrar_info()
    
    cabecario = ['Cod_exercicio', 'Título', 'Descrição', 'Séries', 'Repetições']

    tree = ttk.Treeview(frame_view, selectmode="extended", columns=cabecario, show="headings")

    vsb = ttk.Scrollbar(frame_view, orient="vertical", command=tree.yview)

    hsb = ttk.Scrollbar(frame_view, orient="horizontal", command=tree.xview)


    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_view.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw"]
    h=[50,130,270,70,70]
    n=0

    for col in cabecario:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)


mostrar()
janela.mainloop()



