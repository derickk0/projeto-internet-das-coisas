"""
Nome do arquivo: tela_saida_caminhao.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

import tkinter as tk
from controllers import saida_caminhao

def abrir_tela_saida():
    janela = tk.Toplevel()
    janela.title("Registrar Saída de Caminhão")

    labels = ["Cliente", "Carga", "Destino", "Hora Entrada", "Hora Saída", "KM Inicial", "KM Final"]
    entradas = []

    for i, label in enumerate(labels):
        tk.Label(janela, text=label).grid(row=i, column=0)
        entrada = tk.Entry(janela)
        entrada.grid(row=i, column=1)
        entradas.append(entrada)

    def salvar():
        valores = [e.get() for e in entradas]
        saida_caminhao.registrar_saida(*valores)
        for e in entradas:
            e.delete(0, tk.END)

    tk.Button(janela, text="Registrar", command=salvar).grid(row=len(labels), column=1)
