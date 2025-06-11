"""
Nome do arquivo: caminhoes.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

def adicionar_caminhao(placa, modelo, ano):
    with open("data/caminhoes.txt", "a") as f:
        f.write(f"{placa},{modelo},{ano}\n")

def listar_caminhoes():
    caminhoes = []
    try:
        with open("data/caminhoes.txt", "r") as f:
            for linha in f:
                caminhoes.append(linha.strip().split(","))
    except FileNotFoundError:
        pass
    return caminhoes

def remover_caminhao(placa):
    linhas = listar_caminhoes()
    with open("data/caminhoes.txt", "w") as f:
        for caminhao in linhas:
            if caminhao[0] != placa:
                f.write(",".join(caminhao) + "\n")
