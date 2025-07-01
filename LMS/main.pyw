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
    largura = 1280
    altura = 900
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_vrootheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    root.geometry(f"{largura}x{altura}+{x}+{y}")
    root.title("Last Mile Safety")
    root.iconbitmap("assets/icons/logoIcon.ico")

    try:
        style = ttk.Style(root)
        style.theme_use('vista')
    except:
        style = ttk.Style(root)
        style.theme_use('clam')

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frame_principal = ttk.Frame(root, padding=30)
    frame_principal.pack(expand=True, fill="both")

    label_titulo = ttk.Label(frame_principal, text="LAST MILE SAFETY", font=("Segoe UI", 38, "bold"))
    label_subtitulo = ttk.Label(frame_principal, text="Sistema de Gestão de Transporte e Segurança", font=("Segoe UI", 28))
    label_titulo.pack(pady=(0, 15))
    label_subtitulo.pack(pady=(0, 40))

    frame_botoes = ttk.Frame(frame_principal)
    frame_botoes.pack(expand=True)

    ttk.Button(
        frame_botoes, text="Geral", command=lambda: mostrar_menu("Geral"),
        width=50, style="Main.TButton"
    ).pack(pady=20, ipady=15)
    ttk.Button(
        frame_botoes, text="Oficina", command=lambda: mostrar_menu("Oficina"),
        width=50, style="Main.TButton"
    ).pack(pady=20, ipady=15)
    ttk.Button(
        frame_botoes, text="ADM", command=lambda: mostrar_menu("ADM"),
        width=50, style="Main.TButton"
    ).pack(pady=20, ipady=15)

    def mostrar_menu(menu):
        frame_principal.pack_forget()
        frame_menu = ttk.Frame(root, padding=30)
        frame_menu.pack(expand=True, fill="both")

        def voltar():
            frame_menu.destroy()
            frame_principal.pack(expand=True, fill="both")

        def adm_menu_principal():
            for widget in frame_menu.winfo_children():
                widget.destroy()

            ttk.Label(frame_menu, text="ADM", font=("Segoe UI", 50, "bold")).pack(pady=(0, 15))
            frame_centro = ttk.Frame(frame_menu)
            frame_centro.pack(expand=True)

            ttk.Button(frame_centro, text="Gerenciamento de dados", width=50, style="Menu.TButton",
                       command=adm_gerenciamento).pack(pady=15)
            ttk.Button(frame_centro, text="Controle de Galpão", width=50, style="Menu.TButton",
                       command=adm_galpao).pack(pady=15)
            
            ttk.Button(frame_menu, text="Voltar", width=40, style="Menu.TButton", command=voltar)\
                .pack(side="bottom", pady=(30, 10))

        def adm_gerenciamento():
            for widget in frame_menu.winfo_children():
                widget.destroy()

            ttk.Label(frame_menu, text="Gerenciamento de dados", font=("Segoe UI", 36, "bold")).pack(pady=(0, 15))
            frame_centro = ttk.Frame(frame_menu)
            frame_centro.pack(expand=True)

            botoes = [
                ("Funcionários", tela_funcionarios.abrir_tela_funcionarios),
                ("Fornecedores", tela_fornecedores.abrir_tela_fornecedores),
                ("Clientes", tela_clientes.abrir_tela_clientes),
                ("Produtos", tela_produtos.abrir_tela_produtos),
                ("Caminhões", tela_caminhoes.abrir_tela_caminhoes),
                ("Entrada/Saída", tela_entradaSaida.abrir_tela_entradaSaida),
                ("Manutenções", tela_manutencao.abrir_tela_manutencao),
            ]

            for texto, comando in botoes:
                ttk.Button(frame_centro, text=texto, width=50, style="Menu.TButton", command=comando).pack(pady=8)

            ttk.Button(frame_menu, text="Voltar", width=40, style="Menu.TButton", command=adm_menu_principal)\
                .pack(side="bottom", pady=(30, 10))

        def adm_galpao():
            for widget in frame_menu.winfo_children():
                widget.destroy()

            ttk.Label(frame_menu, text="Controle de Galpão", font=("Segoe UI", 36, "bold")).pack(pady=(0, 15))
            frame_centro = ttk.Frame(frame_menu)
            frame_centro.pack(expand=True)

            botoes = [
                ("Iluminação", tela_iluminacao.abrir_tela_iluminacao),
                ("Sensores", tela_sensores.abrir_tela_sensores),
            ]

            for texto, comando in botoes:
                ttk.Button(frame_centro, text=texto, width=50, style="Menu.TButton", command=comando).pack(pady=15)

            ttk.Button(frame_menu, text="Voltar", width=40, style="Menu.TButton", command=adm_menu_principal)\
                .pack(side="bottom", pady=(30, 10))

        if menu == "ADM":
            adm_menu_principal()
            return

        if menu == "Oficina":
            def oficina_menu_principal():
                for widget in frame_menu.winfo_children():
                    widget.destroy()

                ttk.Label(frame_menu, text="Oficina", font=("Segoe UI", 50, "bold")).pack(pady=(0, 15))
                frame_centro = ttk.Frame(frame_menu)
                frame_centro.pack(expand=True)

                ttk.Button(frame_centro, text="Gerenciamento de dados", width=50, style="Menu.TButton",
                           command=oficina_gerenciamento).pack(pady=15)
                ttk.Button(frame_centro, text="Controle de Galpão", width=50, style="Menu.TButton",
                           command=oficina_galpao).pack(pady=15)
                
                ttk.Button(frame_menu, text="Voltar", width=40, style="Menu.TButton", command=voltar)\
                    .pack(side="bottom", pady=(30, 10))

            def oficina_gerenciamento():
                for widget in frame_menu.winfo_children():
                    widget.destroy()

                ttk.Label(frame_menu, text="Gerenciamento de dados", font=("Segoe UI", 36, "bold")).pack(pady=(0, 15))
                frame_centro = ttk.Frame(frame_menu)
                frame_centro.pack(expand=True)

                botoes = [
                    ("Caminhões", tela_caminhoes.abrir_tela_caminhoes),
                    ("Entrada/Saída", tela_entradaSaida.abrir_tela_entradaSaida),
                    ("Manutenções", tela_manutencao.abrir_tela_manutencao),
                ]

                for texto, comando in botoes:
                    ttk.Button(frame_centro, text=texto, width=50, style="Menu.TButton", command=comando).pack(pady=12)

                ttk.Button(frame_menu, text="Voltar", width=40, style="Menu.TButton", command=oficina_menu_principal)\
                    .pack(side="bottom", pady=(30, 10))

            def oficina_galpao():
                for widget in frame_menu.winfo_children():
                    widget.destroy()

                ttk.Label(frame_menu, text="Controle de Galpão", font=("Segoe UI", 36, "bold")).pack(pady=(0, 15))
                frame_centro = ttk.Frame(frame_menu)
                frame_centro.pack(expand=True)

                botoes = [
                    ("Iluminação", tela_iluminacao.abrir_tela_iluminacao),
                    ("Sensores", tela_sensores.abrir_tela_sensores),
                ]

                for texto, comando in botoes:
                    ttk.Button(frame_centro, text=texto, width=50, style="Menu.TButton", command=comando).pack(pady=15)

                ttk.Button(frame_menu, text="Voltar", width=40, style="Menu.TButton", command=oficina_menu_principal)\
                    .pack(side="bottom", pady=(30, 10))

            oficina_menu_principal()
            return

        for widget in frame_menu.winfo_children():
            widget.destroy()
        ttk.Label(frame_menu, text=menu, font=("Segoe UI", 50, "bold")).pack(pady=(0, 40))

        frame_centro = ttk.Frame(frame_menu)
        frame_centro.pack(expand=True)

        if menu == "Geral":
            botoes = [
                ("Funcionários", tela_funcionarios.abrir_tela_funcionarios),
                ("Fornecedores", tela_fornecedores.abrir_tela_fornecedores),
                ("Clientes", tela_clientes.abrir_tela_clientes),
                ("Produtos", tela_produtos.abrir_tela_produtos),
            ]

            for texto, comando in botoes:
                ttk.Button(frame_centro, text=texto, command=comando, width=50, style="Menu.TButton")\
                    .pack(pady=10)
                
            ttk.Button(frame_menu, text="Voltar", command=voltar, width=40, style="Menu.TButton")\
                .pack(side="bottom", pady=(30, 10))

    style = ttk.Style()
    style.configure("Menu.TButton", font=("Segoe UI", 14), padding=8)
    style.configure("Main.TButton", font=("Segoe UI", 15), padding=10)

    root.mainloop()

if __name__ == "__main__":
    main()
