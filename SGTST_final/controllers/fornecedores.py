"""
Nome do arquivo: fornecedores.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

def adicionar_fornecedor(codigo, nome, contato):
    with open("data/fornecedores.txt", "a") as f:
        f.write(f"{codigo},{nome},{contato}\n")

def listar_fornecedores():
    fornecedores = []
    try:
        with open("data/fornecedores.txt", "r") as f:
            for linha in f:
                fornecedores.append(linha.strip().split(","))
    except FileNotFoundError:
        pass
    return fornecedores

def remover_fornecedor(codigo):
    linhas = listar_fornecedores()
    with open("data/fornecedores.txt", "w") as f:
        for fornecedor in linhas:
            if fornecedor[0] != codigo:
                f.write(",".join(fornecedor) + "\n")
