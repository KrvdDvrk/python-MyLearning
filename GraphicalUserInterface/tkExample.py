from tkinter import Button, Entry, Label, StringVar, Tk

janela = Tk()

# widgets (componenetes)
label = Label(janela, text="Nome:")
nome = Entry(janela)

var = StringVar()
mensagem = Label(janela, textvariable=var)


def callback_diga_ola():
    nome_digitado = nome.get()
    var.set(f"Olá {nome_digitado} boas vindas!!!")


diga_ola = Button(janela, text="Diga olá", command=callback_diga_ola)
sair = Button(janela, text="Sair", command=janela.destroy)

"""
-------------
| 1 | 2 |
------------
| 1 | 2 |
"""


# Posiciona
label.grid(columns=1, row=1)
nome.grid(column=2, row=1)
mensagem.grid(column=2, row=2)
diga_ola.grid(column=2, row=3)
sair.grid(column=2, row=4)


# loop de eventos
# gui
# games
# web

janela.mainloop()
