"""
Nome do arquivo: tela_entradaSaida.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from controllers import entradaSaida
from controllers import caminhoes, funcionarios

def abrir_tela_entradaSaida():
    janela = tk.Toplevel()
    largura = 1000
    altura = 550
    janela.geometry(f"{largura}x{altura}")
    janela.title("Entrada e Saída de Caminhões")
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
    frame_cadastro.grid_columnconfigure(0, weight=1)
    frame_cadastro.grid_columnconfigure(1, weight=3)
    for i in range(14):
        frame_cadastro.grid_rowconfigure(i, weight=1)

    campos = [
        ("ID Entrada/Saída", 0), ("Data Entrada", 1), ("Data Saída", 2), ("Hora Entrada", 3), ("Hora Saída", 4),
        ("Destino", 5), ("Roteiro", 6), ("Peso", 7), ("KM Chegada", 8), ("KM Saída", 9), ("ID Caminhão", 10), ("ID Motorista", 11)
    ]
    entradas = []
    for label, row in campos:
        ttk.Label(frame_cadastro, text=label).grid(row=row, column=0, sticky="e", pady=5, padx=5)
        entry = ttk.Entry(frame_cadastro)
        entry.grid(row=row, column=1, sticky="nsew", pady=5, padx=5)
        entradas.append(entry)

    def salvar():
        valores = [e.get() for e in entradas]
        id_entradaSaida = valores[0]
        id_caminhao = valores[10]
        id_motorista = valores[11]
        ids_existentes = [es['idEntradaSaida'] for es in entradaSaida.listar_entradaSaida()]
        if id_entradaSaida in ids_existentes:
            messagebox.showerror("Erro", f"Já existe um registro com o ID {id_entradaSaida}.")
            return
        ids_caminhao_existentes = [c['idCaminhao'] for c in caminhoes.listar_caminhoes()]
        if id_caminhao not in ids_caminhao_existentes:
            messagebox.showerror("Erro", f"Não existe caminhão cadastrado com o ID {id_caminhao}.")
            return
        ids_funcionarios = [f['idFuncionario'] if 'idFuncionario' in f else f.get('id') for f in funcionarios.listar_funcionarios_dados()]
        if id_motorista not in ids_funcionarios:
            messagebox.showerror("Erro", f"Não existe motorista cadastrado com o ID {id_motorista}.")
            return
        entradaSaida.adicionar_entradaSaida(*valores)
        for e in entradas:
            e.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Registro de entrada/saída cadastrado com sucesso!")

    def mostrar_cadastro():
        frame_lista.grid_forget()
        frame_cadastro.grid(row=0, column=0, sticky="nsew")

    def mostrar_lista():
        frame_cadastro.grid_forget()
        frame_lista.grid(row=0, column=0, sticky="nsew")
        atualizar_lista()

    ttk.Button(frame_cadastro, text="Salvar", command=salvar).grid(row=12, column=0, columnspan=2, sticky="nsew", pady=5, padx=20)
    ttk.Button(frame_cadastro, text="Ir para Lista de Entradas/Saídas", command=mostrar_lista).grid(row=13, column=0, columnspan=2, sticky="nsew", pady=5, padx=20)

    # Frame da lista
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
    lista = tk.Listbox(lista_scroll_frame, width=120, yscrollcommand=scrollbar.set, selectmode=tk.EXTENDED, font=("Segoe UI", 10))
    lista.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
    scrollbar.config(command=lista.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    def atualizar_lista():
        lista.delete(0, tk.END)
        dados = entradaSaida.listar_entradaSaida()
        for es in dados:
            lista.insert(tk.END, f"ID: {es.get('idEntradaSaida', '')} | Caminhão: {es.get('idCaminhao', '')} | Motorista: {es.get('idMotorista', '')} | Entrada: {es.get('dataEntrada', '')} {es.get('horaEntrada', '')} | Saída: {es.get('dataSaida', '')} {es.get('horaSaida', '')}")
            lista.insert(tk.END, f"Destino: {es.get('destino', '')} | Roteiro: {es.get('roteiro', '')} | Peso: {es.get('peso', '')} | KM Chegada: {es.get('kmChegada', '')} | KM Saída: {es.get('kmSaida', '')}")
            lista.insert(tk.END, "-" * 100)

    def on_select(event):
        selecionado = lista.curselection()
        if selecionado:
            idx = selecionado[0]
            bloco_inicio = (idx // 3) * 3
            lista.selection_clear(0, tk.END)
            for i in range(bloco_inicio, bloco_inicio + 3):
                lista.selection_set(i)

    lista.bind('<<ListboxSelect>>', on_select)

    def excluir_entradaSaida():
        selecionado = lista.curselection()
        if selecionado:
            idx = selecionado[0]
            entradaSaida_idx = idx // 3
            dados = entradaSaida.listar_entradaSaida()
            if entradaSaida_idx < len(dados):
                entradaSaida.excluir_entradaSaida(dados[entradaSaida_idx]['idEntradaSaida'])
                atualizar_lista()

    btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", command=excluir_entradaSaida, width=20)
    btn_excluir.grid(row=1, column=0, pady=5, sticky="nsew")
    btn_voltar = ttk.Button(frame_lista, text="Voltar", command=mostrar_cadastro, width=20)
    btn_voltar.grid(row=2, column=0, pady=5, sticky="nsew")

    frame_cadastro.grid(row=0, column=0, sticky="nsew")
