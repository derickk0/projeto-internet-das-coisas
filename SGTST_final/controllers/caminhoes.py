"""
Nome do arquivo: caminhoes.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

def adicionar_caminhao(idCaminhao, renavan, modelo, marca, cor, placa, chassi, status, tipo, peso):
    with open("data/caminhoes.txt", "a") as f:
        f.write(f"{idCaminhao},{renavan},{modelo},{marca},{cor},{placa},{chassi},{status},{tipo},{peso}\n")

def listar_caminhoes():
    caminhoes = []
    try:
        with open("data/caminhoes.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 10:
                    caminhoes.append({
                        'idCaminhao': partes[0],
                        'renavan': partes[1],
                        'modelo': partes[2],
                        'marca': partes[3],
                        'cor': partes[4],
                        'placa': partes[5],
                        'chassi': partes[6],
                        'status': partes[7],
                        'tipo': partes[8],
                        'peso': partes[9]
                    })
    except FileNotFoundError:
        pass
    return caminhoes

def excluir_caminhao(idCaminhao):
    caminhoes = []
    try:
        with open("data/caminhoes.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 10 and partes[0] != idCaminhao:
                    caminhoes.append(linha.strip())
    except FileNotFoundError:
        pass
    
    with open("data/caminhoes.txt", "w") as f:
        for caminhao in caminhoes:
            f.write(caminhao + "\n")
