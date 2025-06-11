"""
Nome do arquivo: pecas.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

def adicionar_peca(codigo, nome, quantidade, fornecedor):
    with open("data/pecas.txt", "a") as f:
        f.write(f"{codigo},{nome},{quantidade},{fornecedor}\n")

def listar_pecas():
    pecas = []
    try:
        with open("data/pecas.txt", "r") as f:
            for linha in f:
                pecas.append(linha.strip().split(","))
    except FileNotFoundError:
        pass
    return pecas

def remover_peca(codigo):
    linhas = listar_pecas()
    with open("data/pecas.txt", "w") as f:
        for peca in linhas:
            if peca[0] != codigo:
                f.write(",".join(peca) + "\n")
