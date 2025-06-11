"""
Nome do arquivo: tela_sensores.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

import tkinter as tk
import random

def abrir_tela_sensores():
    janela = tk.Toplevel()
    janela.title("Simulação de Sensores")

    labels = {
        "Presença": tk.StringVar(),
        "Temperatura": tk.StringVar(),
        "Luminosidade": tk.StringVar(),
        "Fumaça": tk.StringVar()
    }

    row = 0
    for nome, var in labels.items():
        tk.Label(janela, text=nome).grid(row=row, column=0)
        tk.Label(janela, textvariable=var).grid(row=row, column=1)
        row += 1

    def atualizar():
        labels["Presença"].set("Detectado" if random.choice([True, False]) else "Ausente")
        labels["Temperatura"].set(f"{random.randint(20, 50)} °C")
        labels["Luminosidade"].set(f"{random.randint(100, 900)} lux")
        labels["Fumaça"].set("Alerta" if random.random() > 0.8 else "Normal")
        janela.after(2000, atualizar)

    atualizar()
