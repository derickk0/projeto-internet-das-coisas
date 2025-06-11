"""
Nome do arquivo: saida_caminhao.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

def registrar_saida(cliente, carga, destino, entrada, saida, km_inicial, km_final):
    with open("data/saidas.txt", "a") as f:
        f.write(f"{cliente},{carga},{destino},{entrada},{saida},{km_inicial},{km_final}\n")

def listar_saidas():
    saidas = []
    try:
        with open("data/saidas.txt", "r") as f:
            for linha in f:
                saidas.append(linha.strip().split(","))
    except FileNotFoundError:
        pass
    return saidas
