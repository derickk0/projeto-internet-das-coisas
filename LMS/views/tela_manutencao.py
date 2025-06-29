"""
Nome do arquivo: tela_manutencao.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controllers import manutencao, caminhoes
from controllers import funcionarios

def abrir_tela_manutencao():
    janela = tk.Toplevel()
    largura = 900
    altura = 500
    janela.geometry(f"{largura}x{altura}")
    janela.title("Manutenções")
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
    frame_cadastro.grid_columnconfigure(0, weight=1)
    frame_cadastro.grid_columnconfigure(1, weight=3)
    for i in range(9):
        frame_cadastro.grid_rowconfigure(i, weight=1)

    campos = [
        ("ID Manutenção", 0), ("ID Caminhão", 1), ("Data de Início", 2), ("Data de Fim", 3), ("Serviço", 4),
        ("ID Mecânico", 5), ("Peças", 6)
    ]
    entradas = []
    for label, row in campos:
        ttk.Label(frame_cadastro, text=label).grid(row=row, column=0, sticky="e", pady=5, padx=5)
        entry = ttk.Entry(frame_cadastro)
        entry.grid(row=row, column=1, sticky="nsew", pady=5, padx=5)
        entradas.append(entry)

    def salvar():
        valores = [e.get() for e in entradas]
        id_manut = valores[0]
        id_caminhao = valores[1]
        id_mecanico = valores[5]
        ids_manut_existentes = [m['idManutencao'] for m in manutencao.listar_manutencoes()]
        if id_manut in ids_manut_existentes:
            messagebox.showerror("Erro", f"Já existe uma manutenção com o ID {id_manut}.")
            return
        ids_caminhao_existentes = [c['idCaminhao'] for c in caminhoes.listar_caminhoes()]
        if id_caminhao not in ids_caminhao_existentes:
            messagebox.showerror("Erro", f"Não existe caminhão cadastrado com o ID {id_caminhao}.")
            return
        ids_funcionarios = [f['idFuncionario'] for f in funcionarios.listar_funcionarios_dados()]
        if id_mecanico not in ids_funcionarios:
            messagebox.showerror("Erro", f"Não existe funcionário mecânico cadastrado com o ID {id_mecanico}.")
            return
        manutencao.adicionar_manutencao(*valores)
        for e in entradas:
            e.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Manutenção cadastrada com sucesso!")

    def mostrar_cadastro():
        frame_lista.grid_forget()
        frame_cadastro.grid(row=0, column=0, sticky="nsew")

    def mostrar_lista():
        frame_cadastro.grid_forget()
        frame_lista.grid(row=0, column=0, sticky="nsew")
        atualizar_lista()

    ttk.Button(frame_cadastro, text="Salvar", command=salvar).grid(row=7, column=0, columnspan=2, sticky="nsew", pady=5, padx=20)
    ttk.Button(frame_cadastro, text="Ir para Lista de Manutenções", command=mostrar_lista).grid(row=8, column=0, columnspan=2, sticky="nsew", pady=5, padx=20)

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
        dados = manutencao.listar_manutencoes()
        for m in dados:
            lista.insert(tk.END, f"ID: {m.get('idManutencao', '')} | Caminhão: {m.get('idCaminhao', '')} | Início: {m.get('dataInicio', '')} | Fim: {m.get('dataFim', '')}")
            lista.insert(tk.END, f"Serviço: {m.get('servico', '')} | ID do Mecânico: {m.get('mecanico', '')} | Peças: {m.get('idPeca', '')}")
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

    def excluir_manutencao():
        selecionado = lista.curselection()
        if selecionado:
            idx = selecionado[0]
            manutencao_idx = idx // 3
            dados = manutencao.listar_manutencoes()
            if manutencao_idx < len(dados):
                manutencao.excluir_manutencao(dados[manutencao_idx]['idManutencao'])
                atualizar_lista()

    btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", command=excluir_manutencao, width=20)
    btn_excluir.grid(row=1, column=0, pady=5, sticky="nsew")
    btn_voltar = ttk.Button(frame_lista, text="Voltar", command=mostrar_cadastro, width=20)
    btn_voltar.grid(row=2, column=0, pady=5, sticky="nsew")

    frame_cadastro.grid(row=0, column=0, sticky="nsew")
