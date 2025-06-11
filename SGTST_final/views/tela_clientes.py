"""
Nome do arquivo: tela_clientes.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

import tkinter as tk
from controllers import clientes

def abrir_tela_clientes():
    janela = tk.Toplevel()
    janela.title("Cadastro de Clientes")

    tk.Label(janela, text="CNPJ").grid(row=0, column=0)
    tk.Label(janela, text="Nome").grid(row=1, column=0)
    tk.Label(janela, text="Endereço").grid(row=2, column=0)

    cnpj = tk.Entry(janela)
    nome = tk.Entry(janela)
    endereco = tk.Entry(janela)

    cnpj.grid(row=0, column=1)
    nome.grid(row=1, column=1)
    endereco.grid(row=2, column=1)

    def salvar():
        clientes.adicionar_cliente(cnpj.get(), nome.get(), endereco.get())
        cnpj.delete(0, tk.END)
        nome.delete(0, tk.END)
        endereco.delete(0, tk.END)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, column=1)
