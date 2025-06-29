"""
Nome do arquivo: funcionarios.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

def adicionar_funcionario(idFuncionario, cpf, nome, cargo, dataNascimento, telefone, celular, email, logradouro, numero, bairro, cidade, uf, cep, complemento):
    with open("data/funcionarios.txt", "a") as f:
        f.write(f"{idFuncionario},{cpf},{nome},{cargo},{dataNascimento},{telefone},{celular},{email},{logradouro},{numero},{bairro},{cidade},{uf},{cep},{complemento}\n")

def listar_funcionarios_dados():
    funcionarios = []
    try:
        with open("data/funcionarios.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 15:
                    funcionarios.append({
                        'idFuncionario': partes[0],
                        'cpf': partes[1],
                        'nome': partes[2],
                        'cargo': partes[3],
                        'dataNascimento': partes[4],
                        'telefone': partes[5],
                        'celular': partes[6],
                        'email': partes[7]
                    })
    except FileNotFoundError:
        pass
    return funcionarios

def listar_funcionarios_endereco():
    funcionarios = []
    try:
        with open("data/funcionarios.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 15:
                    funcionarios.append({
                        'logradouro': partes[8],
                        'numero': partes[9],
                        'bairro': partes[10],
                        'cidade': partes[11],
                        'uf': partes[12],
                        'cep': partes[13],
                        'complemento': partes[14]
                    })
    except FileNotFoundError:
        pass
    return funcionarios

def excluir_funcionario(idFuncionario):
    funcionarios_dados = []
    try:
        with open("data/funcionarios.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 15 and partes[0] != idFuncionario:
                    funcionarios_dados.append(linha.strip())
    except FileNotFoundError:
        pass
    
    with open("data/funcionarios.txt", "w") as f:
        for funcionario in funcionarios_dados:
            f.write(funcionario + "\n")