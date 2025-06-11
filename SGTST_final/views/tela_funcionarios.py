"""
Nome do arquivo: tela_funcionarios.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

import tkinter as tk
from controllers import funcionarios

def abrir_tela_funcionarios():
    janela = tk.Toplevel()
    janela.title("Cadastro de Funcionários")

    tk.Label(janela, text="CPF").grid(row=0, column=0)
    tk.Label(janela, text="Nome").grid(row=1, column=0)
    tk.Label(janela, text="Cargo").grid(row=2, column=0)

    cpf = tk.Entry(janela)
    nome = tk.Entry(janela)
    cargo = tk.Entry(janela)

    cpf.grid(row=0, column=1)
    nome.grid(row=1, column=1)
    cargo.grid(row=2, column=1)

    def salvar():
        funcionarios.adicionar_funcionario(cpf.get(), nome.get(), cargo.get())
        cpf.delete(0, tk.END)
        nome.delete(0, tk.END)
        cargo.delete(0, tk.END)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, column=1)
