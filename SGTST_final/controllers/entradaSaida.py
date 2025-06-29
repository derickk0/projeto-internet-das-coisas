"""
Nome do arquivo: entradaSaida.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

def adicionar_entradaSaida(idEntradaSaida, dataEntrada, dataSaida, horaEntrada, horaSaida, destino, roteiro, peso, kmChegada, kmSaida, idCaminhao, idMotorista):
    with open("data/entrada_saida.txt", "a") as f:
        f.write(f"{idEntradaSaida},{dataEntrada},{dataSaida},{horaEntrada},{horaSaida},{destino},{roteiro},{peso},{kmChegada},{kmSaida},{idCaminhao},{idMotorista}\n")

def listar_entradaSaida():
    entradaSaida = []
    try:
        with open("data/entrada_saida.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 12:
                    entradaSaida.append({
                        'idEntradaSaida': partes[0],
                        'dataEntrada': partes[1],
                        'dataSaida': partes[2],
                        'horaEntrada': partes[3],
                        'horaSaida': partes[4],
                        'destino': partes[5],
                        'roteiro': partes[6],
                        'peso': partes[7],
                        'kmChegada': partes[8],
                        'kmSaida': partes[9],
                        'idCaminhao': partes[10],
                        'idMotorista': partes[11]
                    })
    except FileNotFoundError:
        pass
    return entradaSaida

def excluir_entradaSaida(idEntradaSaida):
    entradaSaida = []
    try:
        with open("data/entrada_saida.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 12 and partes[0] != idEntradaSaida:
                    entradaSaida.append(linha.strip())
    except FileNotFoundError:
        pass
    
    with open("data/entrada_saida.txt", "w") as f:
        f.writelines(entradaSaida)