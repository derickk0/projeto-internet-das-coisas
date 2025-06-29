"""
Nome do arquivo: tela_clientes.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controllers import clientes

def abrir_tela_clientes():
    janela = tk.Toplevel()
    largura = 900
    altura = 565
    janela.geometry(f"{largura}x{altura}")
    janela.title("Clientes")
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
    janela.grid_columnconfigure(0, weight=1)

    # Frame de cadastro
    frame_cadastro = ttk.Frame(janela, padding=10)
    frame_cadastro.grid(row=0, column=0, sticky="nsew")
    for i in range(2):
        frame_cadastro.grid_columnconfigure(i, weight=1)
    for i in range(15):
        frame_cadastro.grid_rowconfigure(i, weight=1)

    campos = [
        ("ID", 0), ("Nome", 1), ("CPF", 2), ("Telefone", 3), ("Celular", 4), ("Email", 5),
        ("Logradouro", 6), ("Número", 7), ("Bairro", 8), ("Cidade", 9), ("UF", 10), ("CEP", 11), ("Complemento", 12)
    ]
    entradas = []
    for label, row in campos:
        ttk.Label(frame_cadastro, text=label).grid(row=row, column=0, sticky="e", pady=5, padx=5)
        entry = ttk.Entry(frame_cadastro)
        entry.grid(row=row, column=1, sticky="ew", pady=5, padx=5)
        entradas.append(entry)

    def salvar():
        valores = [e.get() for e in entradas]
        id_cliente = valores[0]
        ids_existentes = [c['id'] for c in clientes.listar_clientes_dados()]
        if id_cliente in ids_existentes:
            messagebox.showerror("Erro", f"Já existe um cliente com o ID {id_cliente}.")
            return
        clientes.adicionar_cliente(*valores)
        for e in entradas:
            e.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

    def mostrar_cadastro():
        frame_lista.grid_forget()
        frame_cadastro.grid(row=0, column=0, sticky="nsew")

    def mostrar_lista():
        frame_cadastro.grid_forget()
        frame_lista.grid(row=0, column=0, sticky="nsew")
        atualizar_lista()

    ttk.Button(frame_cadastro, text="Salvar", command=salvar).grid(row=13, column=0, columnspan=2, sticky="nsew", pady=5, padx=20)
    ttk.Button(frame_cadastro, text="Ir para Lista de Clientes", command=mostrar_lista).grid(row=14, column=0, columnspan=2, sticky="ew", pady=5, padx=20)

    # Frame da lista
    frame_lista = ttk.Frame(janela, padding=10)
    frame_lista.grid_rowconfigure(0, weight=1)
    frame_lista.grid_columnconfigure(0, weight=1)
    frame_lista.grid_rowconfigure(1, weight=0)
    frame_lista.grid_rowconfigure(2, weight=0)

    lista_scroll_frame = ttk.Frame(frame_lista)
    lista_scroll_frame.grid(row=0, column=0, sticky="nsew")
    lista_scroll_frame.grid_rowconfigure(0, weight=1)
    lista_scroll_frame.grid_columnconfigure(0, weight=1)

    scrollbar = ttk.Scrollbar(lista_scroll_frame, orient="vertical")
    lista = tk.Listbox(lista_scroll_frame, width=100, yscrollcommand=scrollbar.set, selectmode=tk.EXTENDED, font=("Segoe UI", 10))
    lista.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
    scrollbar.config(command=lista.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    def atualizar_lista():
        lista.delete(0, tk.END)
        dados = clientes.listar_clientes_dados()
        try:
            with open("data/clientes.txt", "r") as f:
                linhas = f.readlines()
        except FileNotFoundError:
            linhas = []
        for i, cli in enumerate(dados):
            lista.insert(tk.END, f"ID: {cli.get('id', '')} | Nome: {cli.get('nome', '')} | CPF: {cli.get('cpf', '')}")
            lista.insert(tk.END, f"Telefone: {cli.get('telefone', '')} | Celular: {cli.get('celular', '')} | Email: {cli.get('email', '')}")
            if i < len(linhas):
                partes = linhas[i].strip().split(",")
                if len(partes) >= 13:
                    endereco = f"Logradouro: {partes[6]} | Número: {partes[7]} | Bairro: {partes[8]} | Cidade: {partes[9]} | UF: {partes[10]} | CEP: {partes[11]} | Complemento: {partes[12]}"
                    lista.insert(tk.END, endereco)
            lista.insert(tk.END, "-" * 80)

    def on_select(event):
        selecionado = lista.curselection()
        if selecionado:
            idx = selecionado[0]
            bloco_inicio = (idx // 4) * 4
            lista.selection_clear(0, tk.END)
            for i in range(bloco_inicio, bloco_inicio + 4):
                lista.selection_set(i)

    lista.bind('<<ListboxSelect>>', on_select)

    def excluir_cliente():
        selecionado = lista.curselection()
        if selecionado:
            idx = selecionado[0]
            cliente_idx = idx // 4
            dados = clientes.listar_clientes_dados()
            if cliente_idx < len(dados):
                clientes.excluir_cliente(dados[cliente_idx]['id'])
                atualizar_lista()

    btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", command=excluir_cliente, width=20)
    btn_excluir.grid(row=1, column=0, pady=5, sticky="ew")
    btn_voltar = ttk.Button(frame_lista, text="Voltar", command=mostrar_cadastro, width=20)
    btn_voltar.grid(row=2, column=0, pady=5, sticky="ew")

    frame_cadastro.grid(row=0, column=0, sticky="nsew")
