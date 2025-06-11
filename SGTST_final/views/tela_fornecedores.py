"""
Nome do arquivo: tela_fornecedores.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

import tkinter as tk
from controllers import fornecedores

def abrir_tela_fornecedores():
    janela = tk.Toplevel()
    janela.title("Cadastro de Fornecedores")

    tk.Label(janela, text="Código").grid(row=0, column=0)
    tk.Label(janela, text="Nome").grid(row=1, column=0)
    tk.Label(janela, text="Contato").grid(row=2, column=0)

    cod = tk.Entry(janela)
    nome = tk.Entry(janela)
    contato = tk.Entry(janela)

    cod.grid(row=0, column=1)
    nome.grid(row=1, column=1)
    contato.grid(row=2, column=1)

    def salvar():
        fornecedores.adicionar_fornecedor(cod.get(), nome.get(), contato.get())
        cod.delete(0, tk.END)
        nome.delete(0, tk.END)
        contato.delete(0, tk.END)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, column=1)
