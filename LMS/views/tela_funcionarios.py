"""
Nome do arquivo: tela_funcionarios.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controllers import funcionarios

def abrir_tela_funcionarios():
    janela = tk.Toplevel()
    largura = 900
    altura = 565
    janela.geometry(f"{largura}x{altura}")
    janela.title("Funcionários")
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

    janela.grid_rowconfigure(0, weight=1)
    janela.grid_columnconfigure(0, weight=1)

    frame_cadastro = ttk.Frame(janela, padding=10)
    frame_cadastro.grid(row=0, column=0, sticky="nsew")
    for i in range(2):
        frame_cadastro.grid_columnconfigure(i, weight=1)
    for i in range(16):
        frame_cadastro.grid_rowconfigure(i, weight=1)

    campos = [
        ("ID Funcionário", 0), ("CPF", 1), ("Nome", 2), ("Cargo", 3), ("Data de Nascimento", 4),
        ("Telefone", 5), ("Celular", 6), ("Email", 7),
        ("Logradouro", 8), ("Número", 9), ("Bairro", 10), ("Cidade", 11), ("UF", 12), ("CEP", 13), ("Complemento", 14)
    ]
    entradas = []
    for label, row in campos:
        ttk.Label(frame_cadastro, text=label).grid(row=row, column=0, sticky="e", pady=5, padx=5)
        entry = ttk.Entry(frame_cadastro)
        entry.grid(row=row, column=1, sticky="ew", pady=5, padx=5)
        entradas.append(entry)

    def salvar():
        valores = [e.get() for e in entradas]
        id_func = valores[0]
        ids_existentes = [f['idFuncionario'] for f in funcionarios.listar_funcionarios_dados()]
        if id_func in ids_existentes:
            messagebox.showerror("Erro", f"Já existe um funcionário com o ID {id_func}.")
            return
        funcionarios.adicionar_funcionario(*valores)
        for e in entradas:
            e.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")

    def mostrar_cadastro():
        frame_lista.grid_forget()
        frame_cadastro.grid(row=0, column=0, sticky="nsew")

    def mostrar_lista():
        frame_cadastro.grid_forget()
        frame_lista.grid(row=0, column=0, sticky="nsew")
        atualizar_lista()

    ttk.Button(frame_cadastro, text="Salvar", command=salvar).grid(row=15, column=0, columnspan=2, sticky="ew", pady=5, padx=20)
    ttk.Button(frame_cadastro, text="Ir para Lista de Funcionários", command=mostrar_lista).grid(row=16, column=0, columnspan=2, sticky="ew", pady=5, padx=20)

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
        dados = funcionarios.listar_funcionarios_dados()
        try:
            with open("data/funcionarios.txt", "r") as f:
                linhas = f.readlines()
        except FileNotFoundError:
            linhas = []
        for i, func in enumerate(dados):
            lista.insert(tk.END, f"ID: {func.get('idFuncionario', '')} | CPF: {func.get('cpf', '')} | Nome: {func.get('nome', '')} | Cargo: {func.get('cargo', '')} | Data de nascimento: {func.get('dataNascimento', '')}")
            lista.insert(tk.END, f"Telefone: {func.get('telefone', '')} | Celular: {func.get('celular', '')} | Email: {func.get('email', '')}")
            if i < len(linhas):
                partes = linhas[i].strip().split(",")
                if len(partes) >= 14:
                    endereco = f"Logradouro: {partes[8]} | Número: {partes[9]} | Bairro: {partes[10]} | Cidade: {partes[11]} | UF: {partes[12]} | CEP: {partes[13]} | Complemento: {partes[14]}"
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

    def excluir_funcionario():
        selecionado = lista.curselection()
        if selecionado:
            idx = selecionado[0]
            funcionario_idx = idx // 4
            dados = funcionarios.listar_funcionarios_dados()
            if funcionario_idx < len(dados):
                funcionarios.excluir_funcionario(dados[funcionario_idx]['idFuncionario'])
                atualizar_lista()

    btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", command=excluir_funcionario, width=20)
    btn_excluir.grid(row=1, column=0, pady=5, sticky="ew")
    btn_voltar = ttk.Button(frame_lista, text="Voltar", command=mostrar_cadastro, width=20)
    btn_voltar.grid(row=2, column=0, pady=5, sticky="ew")

    frame_cadastro.grid(row=0, column=0, sticky="nsew")

