"""
Nome do arquivo: tela_pecas.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

import tkinter as tk
from controllers import pecas

def abrir_tela_pecas():
    janela = tk.Toplevel()
    janela.title("Cadastro de Peças")

    tk.Label(janela, text="Código").grid(row=0, column=0)
    tk.Label(janela, text="Nome").grid(row=1, column=0)
    tk.Label(janela, text="Quantidade").grid(row=2, column=0)
    tk.Label(janela, text="Fornecedor").grid(row=3, column=0)

    cod = tk.Entry(janela)
    nome = tk.Entry(janela)
    qtd = tk.Entry(janela)
    forn = tk.Entry(janela)

    cod.grid(row=0, column=1)
    nome.grid(row=1, column=1)
    qtd.grid(row=2, column=1)
    forn.grid(row=3, column=1)

    def salvar():
        pecas.adicionar_peca(cod.get(), nome.get(), qtd.get(), forn.get())
        cod.delete(0, tk.END)
        nome.delete(0, tk.END)
        qtd.delete(0, tk.END)
        forn.delete(0, tk.END)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=4, column=1)
