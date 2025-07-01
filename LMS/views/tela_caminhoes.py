"""
Nome do arquivo: tela_caminhoes.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controllers import caminhoes

def abrir_tela_caminhoes():
    janela = tk.Toplevel()
    largura = 900
    altura = 520
    janela.geometry(f"{largura}x{altura}")
    janela.title("Caminhões")
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

    frame_cadastro = ttk.Frame(janela, padding=10)
    frame_cadastro.pack(expand=True, fill="both")
    frame_cadastro.grid_columnconfigure(0, weight=1)
    frame_cadastro.grid_columnconfigure(1, weight=3)
    for i in range(12):
        frame_cadastro.grid_rowconfigure(i, weight=1)

    campos = [
        ("ID Caminhão", 0), ("Renavan", 1), ("Modelo", 2), ("Marca", 3), ("Cor", 4),
        ("Placa", 5), ("Chassi", 6), ("Status", 7), ("Tipo", 8), ("Peso", 9)
    ]
    entradas = []
    for label, row in campos:
        ttk.Label(frame_cadastro, text=label).grid(row=row, column=0, sticky="e", pady=5, padx=5)
        entry = ttk.Entry(frame_cadastro)
        entry.grid(row=row, column=1, sticky="nsew", pady=5, padx=5)
        entradas.append(entry)

    def salvar():
        valores = [e.get() for e in entradas]
        id_caminhao = valores[0]
        ids_existentes = [c['idCaminhao'] for c in caminhoes.listar_caminhoes()]

        if id_caminhao in ids_existentes:
            messagebox.showerror("Erro", f"Já existe um caminhão com o ID {id_caminhao}.")
            return
        
        caminhoes.adicionar_caminhao(*valores)

        for e in entradas:
            e.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Caminhão cadastrado com sucesso!")

    def mostrar_cadastro():
        frame_lista.pack_forget()
        frame_cadastro.pack(expand=True, fill="both")

    def mostrar_lista():
        frame_cadastro.pack_forget()
        frame_lista.pack(expand=True, fill="both")
        atualizar_lista()

    ttk.Button(frame_cadastro, text="Salvar", command=salvar).grid(row=10, column=0, columnspan=2, sticky="nsew", pady=5, padx=20)
    ttk.Button(frame_cadastro, text="Ir para Lista de Caminhões", command=mostrar_lista).grid(row=11, column=0, columnspan=2, sticky="nsew", pady=5, padx=20)

    frame_lista = ttk.Frame(janela, padding=10)
    frame_lista.grid_columnconfigure(0, weight=1)
    frame_lista.grid_rowconfigure(0, weight=1)
    frame_lista.grid_rowconfigure(1, weight=0)
    frame_lista.grid_rowconfigure(2, weight=0)

    lista_scroll_frame = ttk.Frame(frame_lista)
    lista_scroll_frame.grid(row=0, column=0, sticky="nsew")
    lista_scroll_frame.grid_columnconfigure(0, weight=1)

    scrollbar = ttk.Scrollbar(lista_scroll_frame, orient="vertical")
    scrollbar_horizontal = ttk.Scrollbar(lista_scroll_frame, orient="horizontal")

    lista = tk.Listbox(
        lista_scroll_frame,
        width=100,
        yscrollcommand=scrollbar.set,
        xscrollcommand=scrollbar_horizontal.set,
        selectmode=tk.EXTENDED,
        font=("Segoe UI", 10)
    )

    lista.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
    scrollbar.config(command=lista.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    scrollbar_horizontal.config(command=lista.xview)
    scrollbar_horizontal.grid(row=1, column=0, sticky="ew", padx=10)
    lista_scroll_frame.grid_rowconfigure(0, weight=1)
    lista_scroll_frame.grid_columnconfigure(0, weight=1)

    def atualizar_lista():
        lista.delete(0, tk.END)
        dados = caminhoes.listar_caminhoes()

        for c in dados:
            lista.insert(tk.END, f"ID: {c.get('idCaminhao', '')} | Renavan: {c.get('renavan', '')} | Modelo: {c.get('modelo', '')} | Marca: {c.get('marca', '')} | Cor: {c.get('cor', '')}")
            lista.insert(tk.END, f"Placa: {c.get('placa', '')} | Chassi: {c.get('chassi', '')} | Status: {c.get('status', '')} | Tipo: {c.get('tipo', '')} | Peso: {c.get('peso', '')}")
            lista.insert(tk.END, "-" * 80)

    def on_select(event):
        selecionado = lista.curselection()

        if selecionado:
            idx = selecionado[0]
            bloco_inicio = (idx // 3) * 3
            lista.selection_clear(0, tk.END)
            for i in range(bloco_inicio, bloco_inicio + 3):
                lista.selection_set(i)

    lista.bind('<<ListboxSelect>>', on_select)

    def excluir_caminhao():
        selecionado = lista.curselection()

        if selecionado:
            idx = selecionado[0]
            caminhao_idx = idx // 3
            dados = caminhoes.listar_caminhoes()
            
            if caminhao_idx < len(dados):
                caminhoes.excluir_caminhao(dados[caminhao_idx]['idCaminhao'])
                atualizar_lista()

    btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", command=excluir_caminhao, width=20)
    btn_excluir.grid(row=1, column=0, pady=5, sticky="nsew")
    btn_voltar = ttk.Button(frame_lista, text="Voltar", command=mostrar_cadastro, width=20)
    btn_voltar.grid(row=2, column=0, pady=5, sticky="nsew")

    frame_cadastro.pack(expand=True, fill="both")


