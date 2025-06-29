"""
Nome do arquivo: tela_sensores.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import ttk
import random

def abrir_tela_sensores():
    janela = tk.Toplevel()
    largura = 400
    altura = 250
    janela.geometry(f"{largura}x{altura}")
    janela.title("Sensores")
    janela.transient(janela.master)
    janela.grab_set()
    janela.focus_set()

    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

    try:
        style = ttk.Style(janela)
        style.theme_use('vista')
    except:
        style = ttk.Style(janela)
        style.theme_use('clam')

    janela.grid_rowconfigure(0, weight=1)
    janela.grid_rowconfigure(1, weight=0)
    janela.grid_columnconfigure(0, weight=1)

    frame = ttk.Frame(janela, padding=20)
    frame.grid(row=0, column=0, sticky="nsew")
    for i in range(4):
        frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=2)

    labels = {
        "Presença": tk.StringVar(),
        "Temperatura": tk.StringVar(),
        "Luminosidade": tk.StringVar(),
        "Fumaça": tk.StringVar()
    }

    row = 0
    for nome, var in labels.items():
        ttk.Label(frame, text=nome+":", font=("Segoe UI", 11, "bold")).grid(row=row, column=0, sticky="e", pady=8, padx=8)
        ttk.Label(frame, textvariable=var, font=("Segoe UI", 11)).grid(row=row, column=1, sticky="w", pady=8, padx=8)
        row += 1

    def atualizar():
        labels["Presença"].set("Detectado" if random.choice([True, False]) else "Ausente")
        labels["Temperatura"].set(f"{random.randint(20, 50)} °C")
        labels["Luminosidade"].set(f"{random.randint(100, 900)} lux")
        labels["Fumaça"].set("Alerta" if random.random() > 0.8 else "Normal")
        janela.after(2000, atualizar)

    atualizar()

    btn_fechar = ttk.Button(janela, text="Fechar", command=janela.destroy)
    btn_fechar.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

    janela.mainloop()
