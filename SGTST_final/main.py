"""
Nome do arquivo: main.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

import tkinter as tk
from views import tela_pecas
from views import tela_fornecedores
from views import tela_caminhoes
from views import tela_funcionarios
from views import tela_clientes
from views import tela_saida_caminhao
from views import tela_iluminacao
from views import tela_sensores

def main():
    root = tk.Tk()
    root.title("SGTST - Sistema de Transporte")

    tk.Label(root, text="Bem-vindo ao SGTST").pack(pady=10)

    tk.Button(root, text="Gerenciar Peças", command=tela_pecas.abrir_tela_pecas).pack()

    tk.Button(root, text="Fornecedores", command=tela_fornecedores.abrir_tela_fornecedores).pack()
    tk.Button(root, text="Caminhões", command=tela_caminhoes.abrir_tela_caminhoes).pack()
    tk.Button(root, text="Funcionários", command=tela_funcionarios.abrir_tela_funcionarios).pack()
    tk.Button(root, text="Clientes", command=tela_clientes.abrir_tela_clientes).pack()
    tk.Button(root, text="Saída de Caminhão", command=tela_saida_caminhao.abrir_tela_saida).pack()

    
    # tk.Button(root, text="Controle de Iluminação", command=tela_iluminacao.abrir_tela_iluminacao).pack()
    tk.Button(root, text="Sensores (Simulado)", command=tela_sensores.abrir_tela_sensores).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
