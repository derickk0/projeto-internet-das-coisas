"""
Nome do arquivo: main.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import ttk
from views import tela_produtos
from views import tela_fornecedores
from views import tela_caminhoes
from views import tela_funcionarios
from views import tela_clientes
from views import tela_entradaSaida
from views import tela_iluminacao
from views import tela_sensores
from views import tela_manutencao

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("SGTST - Sistema de Transporte")
    root.state('zoomed')
    try:
        style = ttk.Style(root)
        style.theme_use('vista')
    except:
        style = ttk.Style(root)
        style.theme_use('clam')

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frame_principal = ttk.Frame(root, padding=30)
    frame_principal.grid(row=0, column=0, sticky="nsew")
    frame_principal.grid_rowconfigure(0, weight=1)
    frame_principal.grid_rowconfigure(1, weight=1)
    frame_principal.grid_rowconfigure(2, weight=1)
    frame_principal.grid_rowconfigure(3, weight=1)
    frame_principal.grid_columnconfigure(0, weight=1)

    label_titulo = ttk.Label(frame_principal, text="SGTST - Sistema de Transporte", font=("Segoe UI", 28, "bold"))
    label_titulo.grid(row=0, column=0, pady=(0, 40))

    def mostrar_menu(menu):
        frame_principal.grid_remove()
        frame_menu = ttk.Frame(root, padding=30)
        frame_menu.grid(row=0, column=0, sticky="nsew")
        frame_menu.grid_columnconfigure(0, weight=1)
        frame_menu.grid_rowconfigure(0, weight=1)
        frame_menu.grid_rowconfigure(99, weight=1)
        ttk.Label(frame_menu, text=menu, font=("Segoe UI", 22, "bold")).grid(row=0, column=0, pady=(0, 30))
        row = 1
        def voltar():
            frame_menu.destroy()
            frame_principal.grid()
        if menu == "Geral":
            botoes = [
                ("Funcionários", tela_funcionarios.abrir_tela_funcionarios),
                ("Fornecedores", tela_fornecedores.abrir_tela_fornecedores),
                ("Clientes", tela_clientes.abrir_tela_clientes),
                ("Produtos", tela_produtos.abrir_tela_produtos),
            ]
        elif menu == "Oficina":
            botoes = [
                ("Caminhões", tela_caminhoes.abrir_tela_caminhoes),
                ("Entrada/Saída", tela_entradaSaida.abrir_tela_entradaSaida),
                ("Manutenção", tela_manutencao.abrir_tela_manutencao),
                ("Iluminação", tela_iluminacao.abrir_tela_iluminacao),
                ("Sensores", tela_sensores.abrir_tela_sensores),
            ]
        elif menu == "ADM Geral":
            botoes = [
                ("Funcionários", tela_funcionarios.abrir_tela_funcionarios),
                ("Fornecedores", tela_fornecedores.abrir_tela_fornecedores),
                ("Clientes", tela_clientes.abrir_tela_clientes),
                ("Produtos", tela_produtos.abrir_tela_produtos),
                ("Caminhões", tela_caminhoes.abrir_tela_caminhoes),
                ("Entrada/Saída", tela_entradaSaida.abrir_tela_entradaSaida),
                ("Manutenção", tela_manutencao.abrir_tela_manutencao),
                ("Iluminação", tela_iluminacao.abrir_tela_iluminacao),
                ("Sensores", tela_sensores.abrir_tela_sensores),
            ]
        for texto, comando in botoes:
            ttk.Button(frame_menu, text=texto, command=comando, width=20, style="Menu.TButton").grid(row=row, column=0, pady=7, ipady=7, sticky="nsew")
            row += 1
        ttk.Button(frame_menu, text="Voltar", command=voltar, width=20, style="Menu.TButton").grid(row=row, column=0, pady=(30,0), ipady=7, sticky="nsew")

    style = ttk.Style()
    style.configure("Menu.TButton", font=("Segoe UI", 14), padding=8)
    style.configure("Main.TButton", font=("Segoe UI", 15), padding=10)

    ttk.Button(frame_principal, text="Geral", command=lambda: mostrar_menu("Geral"), width=20, style="Main.TButton").grid(row=1, column=0, pady=10, ipady=10, sticky="nsew")
    ttk.Button(frame_principal, text="Oficina", command=lambda: mostrar_menu("Oficina"), width=20, style="Main.TButton").grid(row=2, column=0, pady=10, ipady=10, sticky="nsew")
    ttk.Button(frame_principal, text="ADM", command=lambda: mostrar_menu("ADM Geral"), width=20, style="Main.TButton").grid(row=3, column=0, pady=10, ipady=10, sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    main()
