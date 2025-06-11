"""
Nome do arquivo: clientes.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

def adicionar_cliente(cnpj, nome, endereco):
    with open("data/clientes.txt", "a") as f:
        f.write(f"{cnpj},{nome},{endereco}\n")

def listar_clientes():
    clientes = []
    try:
        with open("data/clientes.txt", "r") as f:
            for linha in f:
                clientes.append(linha.strip().split(","))
    except FileNotFoundError:
        pass
    return clientes

def remover_cliente(cnpj):
    linhas = listar_clientes()
    with open("data/clientes.txt", "w") as f:
        for cliente in linhas:
            if cliente[0] != cnpj:
                f.write(",".join(cliente) + "\n")
