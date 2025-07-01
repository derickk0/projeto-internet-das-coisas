"""
Nome do arquivo: tela_produtos.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controllers import produtos

def abrir_tela_produtos():
    janela = tk.Toplevel()
    largura = 900
    altura = 500
    janela.geometry(f"{largura}x{altura}")
    janela.title("Produtos")
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
    janela.grid_columnconfigure(0, weight=1)

    frame_cadastro = ttk.Frame(janela, padding=10)
    frame_cadastro.grid(row=0, column=0, sticky="nsew")
    frame_cadastro.grid_columnconfigure(0, weight=1)
    frame_cadastro.grid_columnconfigure(1, weight=3)

    for i in range(10):
        frame_cadastro.grid_rowconfigure(i, weight=1)

    campos = [
        ("Código", 0), ("Fornecedor", 1), ("Nome", 2), ("Descrição", 3), ("Tipo", 4),
        ("Quantidade", 5), ("Validade", 6), ("Observações", 7)
    ]

    entradas = []

    for label, row in campos:
        ttk.Label(frame_cadastro, text=label).grid(row=row, column=0, sticky="e", pady=5, padx=5)
        entry = ttk.Entry(frame_cadastro)
        entry.grid(row=row, column=1, sticky="nsew", pady=5, padx=5)
        entradas.append(entry)

    def salvar():
        valores = [e.get() for e in entradas]
        codigo = valores[0]
        codigos_existentes = [p['codigo'] for p in produtos.listar_produtos()]

        if codigo in codigos_existentes:
            messagebox.showerror("Erro", f"Já existe um produto com o código {codigo}.")
            return
        
        produtos.adicionar_produto(*valores)

        for e in entradas:
            e.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

    def mostrar_cadastro():
        frame_lista.grid_forget()
        frame_cadastro.grid(row=0, column=0, sticky="nsew")

    def mostrar_lista():
        frame_cadastro.grid_forget()
        frame_lista.grid(row=0, column=0, sticky="nsew")
        atualizar_lista()

    ttk.Button(frame_cadastro, text="Salvar", command=salvar).grid(row=8, column=0, columnspan=2, sticky="nsew", pady=5, padx=20)
    ttk.Button(frame_cadastro, text="Ir para Lista de Produtos", command=mostrar_lista).grid(row=9, column=0, columnspan=2, sticky="nsew", pady=5, padx=20)

    frame_lista = ttk.Frame(janela, padding=10)
    frame_lista.grid_columnconfigure(0, weight=1)
    frame_lista.grid_rowconfigure(0, weight=1)
    frame_lista.grid_rowconfigure(1, weight=0)
    frame_lista.grid_rowconfigure(2, weight=0)

    lista_scroll_frame = ttk.Frame(frame_lista)
    lista_scroll_frame.grid(row=0, column=0, sticky="nsew")
    lista_scroll_frame.grid_columnconfigure(0, weight=1)
    lista_scroll_frame.grid_rowconfigure(0, weight=1)

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
        dados = produtos.listar_produtos()

        for p in dados:
            lista.insert(tk.END, f"Código: {p.get('codigo', '')} | Fornecedor: {p.get('fornecedor', '')} | Nome: {p.get('nome', '')} | Tipo: {p.get('tipo', '')}")
            lista.insert(tk.END, f"Descrição: {p.get('descricao', '')} | Quantidade: {p.get('quantidade', '')} | Validade: {p.get('validade', '')}")
            lista.insert(tk.END, f"Observações: {p.get('observacoes', '')}")
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

    def excluir_produto():
        selecionado = lista.curselection()

        if selecionado:
            idx = selecionado[0]
            produto_idx = idx // 4
            dados = produtos.listar_produtos()
            
            if produto_idx < len(dados):
                produtos.excluir_produto(dados[produto_idx]['codigo'])
                atualizar_lista()

    btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", command=excluir_produto, width=20)
    btn_excluir.grid(row=1, column=0, pady=5, sticky="nsew")
    btn_voltar = ttk.Button(frame_lista, text="Voltar", command=mostrar_cadastro, width=20)
    btn_voltar.grid(row=2, column=0, pady=5, sticky="nsew")

    frame_cadastro.grid(row=0, column=0, sticky="nsew")

