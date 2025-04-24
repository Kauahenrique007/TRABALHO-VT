import tkinter as tk
from tkinter import messagebox

#Função que será chamada ao clicar no botão
def mostrar_mensagem():
    nome = entrada_nome.get()
    messagebox.showinfo("Olá!", f"Seja bem-vindo, {nome}!")

#Janela principal
janela = tk.Tk()
janela.title("Interface em Python")

#Título
titulo = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12))
titulo.pack(pady=10)

#Campo de entrada
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack(pady=5)

#Botão
botao = tk.Button(janela, text="Enviar", command=mostrar_mensagem)
botao.pack(pady=20)

#Loop da interface
janela.mainloop()

import tkinter as tk
from tkinter import messagebox

#Função que será chamada ao clicar no botão
def mostrar_mensagem():
    nome = entrada_nome.get()
    messagebox.showinfo("Olá!", f"Seja bem-vindo, {nome}!")

#Janela principal
janela = tk.Tk()
janela.title("Interface em Python")

#Título
titulo = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12))
titulo.pack(pady=10)

#Campo de entrada
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack(pady=5)

#Botão
botao = tk.Button(janela, text="Enviar", command=mostrar_mensagem)
botao.pack(pady=20)

#Loop da interface
janela.mainloop()
