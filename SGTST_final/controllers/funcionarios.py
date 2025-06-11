"""
Nome do arquivo: funcionarios.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

def adicionar_funcionario(cpf, nome, cargo):
    with open("data/funcionarios.txt", "a") as f:
        f.write(f"{cpf},{nome},{cargo}\n")

def listar_funcionarios():
    funcionarios = []
    try:
        with open("data/funcionarios.txt", "r") as f:
            for linha in f:
                funcionarios.append(linha.strip().split(","))
    except FileNotFoundError:
        pass
    return funcionarios

def remover_funcionario(cpf):
    linhas = listar_funcionarios()
    with open("data/funcionarios.txt", "w") as f:
        for funcionario in linhas:
            if funcionario[0] != cpf:
                f.write(",".join(funcionario) + "\n")
