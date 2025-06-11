"""
Nome do arquivo: tela_caminhoes.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

import tkinter as tk
from controllers import caminhoes

def abrir_tela_caminhoes():
    janela = tk.Toplevel()
    janela.title("Cadastro de Caminhões")

    tk.Label(janela, text="Placa").grid(row=0, column=0)
    tk.Label(janela, text="Modelo").grid(row=1, column=0)
    tk.Label(janela, text="Ano").grid(row=2, column=0)

    placa = tk.Entry(janela)
    modelo = tk.Entry(janela)
    ano = tk.Entry(janela)

    placa.grid(row=0, column=1)
    modelo.grid(row=1, column=1)
    ano.grid(row=2, column=1)

    def salvar():
        caminhoes.adicionar_caminhao(placa.get(), modelo.get(), ano.get())
        placa.delete(0, tk.END)
        modelo.delete(0, tk.END)
        ano.delete(0, tk.END)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, column=1)
