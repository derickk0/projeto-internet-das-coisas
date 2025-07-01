"""
Nome do arquivo: tela_sensores.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

# Este código exibe dados fictícios caso não haja conexão com o Arduino
# Em caso de uso real, o arquivo: tela_sensoresUsoReal.py deve ser renomeado e utilizado no lugar deste

import tkinter as tk
from tkinter import ttk, messagebox
import serial
import threading
import re
import random

def get_arduino():
    try:
        return serial.Serial('COM3', 9600, timeout=1)
    except Exception:
        return None

arduino = get_arduino()


def abrir_tela_sensores():
    janela = tk.Toplevel()
    largura = 400
    altura = 250
    janela.geometry(f"{largura}x{altura}")
    janela.title("Sensores")
    janela.iconbitmap("assets/icons/logoIcon.ico")
    janela.transient(janela.master)
    janela.grab_set()
    janela.focus_set()

    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_vrootheight() // 2) - (altura // 2)
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

    for i in range(3):
        frame.grid_rowconfigure(i, weight=1)

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=2)

    labels = {
        "Presença": tk.StringVar(value="---"),
        "Luminosidade": tk.StringVar(value="---"),
        "Temperatura": tk.StringVar(value="---")
    }

    ttk.Label(frame, text="Presença:", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="e", pady=8, padx=8)
    ttk.Label(frame, textvariable=labels["Presença"], font=("Segoe UI", 11)).grid(row=0, column=1, sticky="w", pady=8, padx=8)
    ttk.Label(frame, text="Luminosidade:", font=("Segoe UI", 11, "bold")).grid(row=1, column=0, sticky="e", pady=8, padx=8)
    ttk.Label(frame, textvariable=labels["Luminosidade"], font=("Segoe UI", 11)).grid(row=1, column=1, sticky="w", pady=8, padx=8)
    ttk.Label(frame, text="Temperatura:", font=("Segoe UI", 11, "bold")).grid(row=2, column=0, sticky="e", pady=8, padx=8)
    ttk.Label(frame, textvariable=labels["Temperatura"], font=("Segoe UI", 11)).grid(row=2, column=1, sticky="w", pady=8, padx=8)

    def ler_serial():
        if not arduino or not arduino.is_open:
            labels["Presença"].set("Detectado" if random.choice([True, False]) else "Ausente")
            labels["Luminosidade"].set(str(random.randint(100, 900)))
            tempC = random.uniform(20, 50)
            tempF = tempC * 9.0 / 5.0 + 32.0
            labels["Temperatura"].set(f"{tempC:.1f} °C | {tempF:.1f} °F")
            janela.after(1000, ler_serial)
            return
        try:
            linha = arduino.readline().decode(errors='ignore').strip()
            match = re.search(r'Presenca: (\d+) \| Luminosidade: (\d+) \| Temperatura: ([\d\.-]+)C ([\d\.-]+)F', linha)
            if match:
                presenca = "Detectado" if match.group(1) == "1" else "Ausente"
                luminosidade = match.group(2)
                tempC = match.group(3)
                tempF = match.group(4)
                labels["Presença"].set(presenca)
                labels["Luminosidade"].set(luminosidade)
                labels["Temperatura"].set(f"{tempC} °C | {tempF} °F")
        except Exception:
            pass
        janela.after(1000, ler_serial)

    ler_serial()

    btn_fechar = ttk.Button(janela, text="Fechar", command=janela.destroy)
    btn_fechar.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

    janela.mainloop()
