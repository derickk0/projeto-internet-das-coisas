"""
Nome do arquivo: manutencao.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

def adicionar_manutencao(idManutencao, idCaminhao, dataInicio, dataFim, servico, mecanico, idPeca):
    with open("data/manutencao.txt", "a") as f:
        f.write(f"{idManutencao},{idCaminhao},{dataInicio},{dataFim},{servico},{mecanico},{idPeca}\n")

def listar_manutencoes():
    manutencoes = []
    try:
        with open("data/manutencao.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 7:
                    manutencoes.append({
                        'idManutencao': partes[0],
                        'idCaminhao': partes[1],
                        'dataInicio': partes[2],
                        'dataFim': partes[3],
                        'servico': partes[4],
                        'mecanico': partes[5],
                        'idPeca': partes[6]
                    })
    except FileNotFoundError:
        pass
    return manutencoes

def excluir_manutencao(idManutencao):
    manutencoes = []
    try:
        with open("data/manutencao.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 7 and partes[0] != idManutencao:
                    manutencoes.append(linha.strip())
    except FileNotFoundError:
        pass
    with open("data/manutencao.txt", "w") as f:
        f.writelines(manutencoes)