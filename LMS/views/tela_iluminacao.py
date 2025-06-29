"""
Nome do arquivo: tela_iluminacao.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import ttk, messagebox
import serial

def get_arduino():
    try:
        return serial.Serial('COM3', 9600, timeout=1)
    except Exception:
        return None

arduino = get_arduino()

def enviar_comando(comando):
    if arduino and arduino.is_open:
        try:
            arduino.write(comando.encode())
        except Exception:
            messagebox.showerror("Erro", "Falha ao enviar comando para o Arduino.")
    else:
        messagebox.showerror("Erro", "Arduino não conectado.")

def abrir_tela_iluminacao():
    janela = tk.Toplevel()
    largura, altura = 400, 550
    janela.geometry(f"{largura}x{altura}")
    janela.title("Gerenciamento de Iluminação")
    janela.iconbitmap("assets/icons/logoIcon.ico")
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

    style = ttk.Style()
    style.configure("Ilum.TButton", font=("Segoe UI", 13), padding=8)

    frame_principal = ttk.Frame(janela, padding=30)
    frame_principal.grid(row=0, column=0, sticky="nsew")
    janela.grid_rowconfigure(0, weight=1)
    janela.grid_columnconfigure(0, weight=1)
    frame_principal.grid_columnconfigure(0, weight=1)
    frame_principal.grid_rowconfigure(tuple(range(7)), weight=1)

    def mostrar_menu_principal():
        for widget in frame_principal.winfo_children():
            widget.destroy()
        ttk.Label(frame_principal, text="Gerenciamento de Iluminação", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, pady=(0, 20), sticky="nsew")
        setores = [
            ("Oficina", lambda: mostrar_setor("Oficina")),
            ("Galpão", lambda: mostrar_setor("Galpão")),
            ("Escritório", lambda: mostrar_setor("Escritório")),
            ("Corredor", lambda: mostrar_setor("Corredor")),
            ("Área de serviço", lambda: mostrar_setor("Área de serviço")),
            ("Área externa", lambda: mostrar_setor("Área externa")),
        ]
        for i, (nome, comando) in enumerate(setores, start=1):
            ttk.Button(frame_principal, text=nome, command=comando, style="Ilum.TButton").grid(row=i, column=0, pady=7, ipady=7, sticky="nsew")

    def mostrar_setor(setor):
        for widget in frame_principal.winfo_children():
            widget.destroy()
        botoes = []
        if setor == "Oficina":
            botoes = [
                ("Ligar", lambda: enviar_comando("a")),
                ("Desligar", lambda: enviar_comando("b")),
            ]
        elif setor == "Galpão":
            botoes = [
                ("Ligar todos os Blocos", lambda: enviar_comando("k")),
                ("Ligar Bloco 1", lambda: enviar_comando("l")),
                ("Ligar Bloco 2", lambda: enviar_comando("m")),
                ("Ligar Bloco 3", lambda: enviar_comando("n")),
                ("Apagar todos os Blocos", lambda: enviar_comando("o")),
            ]
        elif setor == "Escritório":
            botoes = [
                ("Ligar", lambda: enviar_comando("c")),
                ("Desligar", lambda: enviar_comando("d")),
            ]
        elif setor == "Corredor":
            botoes = [
                ("Ligar", lambda: enviar_comando("e")),
                ("Desligar", lambda: enviar_comando("f")),
            ]
        elif setor == "Área de serviço":
            botoes = [
                ("Ligar", lambda: enviar_comando("g")),
                ("Desligar", lambda: enviar_comando("h")),
            ]
        elif setor == "Área externa":
            botoes = [
                ("Ligar", lambda: enviar_comando("i")),
                ("Desligar", lambda: enviar_comando("j")),
            ]
        ttk.Label(frame_principal, text=setor, font=("Segoe UI", 15, "bold")).grid(row=0, column=0, pady=(0, 20), sticky="nsew")
        for i, (nome, comando) in enumerate(botoes, start=1):
            ttk.Button(frame_principal, text=nome, command=comando, style="Ilum.TButton").grid(row=i, column=0, pady=7, ipady=7, sticky="nsew")
        def voltar():
            mostrar_menu_principal()
        ttk.Button(frame_principal, text="Voltar", command=voltar, style="Ilum.TButton").grid(row=len(botoes)+1, column=0, pady=(30,0), ipady=7, sticky="nsew")

    mostrar_menu_principal()
