"""
Nome do arquivo: fornecedores.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

def adicionar_fornecedor(cnpj, razaoSocial, nomeFantasia, areaAtuacao, telefone, celular, email, 
                         logradouro, numero, bairro, cidade, uf, cep, complemento, produtos):
    with open("data/fornecedores.txt", "a") as f:
        f.write(f"{cnpj},{razaoSocial},{nomeFantasia},{areaAtuacao},{produtos},{telefone},{celular},{email},{logradouro},{numero},{bairro},{cidade},{uf},{cep},{complemento}\n")

def listar_fornecedores_dados():
    fornecedores = []
    try:
        with open("data/fornecedores.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 15:
                    fornecedores.append({
                        'cnpj': partes[0],
                        'razaoSocial': partes[1],
                        'nomeFantasia': partes[2],
                        'areaAtuacao': partes[3],
                        'produtos': partes[4],
                        'telefone': partes[5],
                        'celular': partes[6],
                        'email': partes[7],
                    })
    except FileNotFoundError:
        pass
    return fornecedores

def listar_fornecedores_endereco():
    fornecedores = []
    try:
        with open("data/fornecedores.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 15:
                    fornecedores.append({
                        'logradouro': partes[0],
                        'numero': partes[1],
                        'bairro': partes[2],
                        'cidade': partes[3],
                        'uf': partes[4],
                        'cep': partes[5],
                        'complemento': partes[6]
                    })
    except FileNotFoundError:
        pass
    return fornecedores

def excluir_fornecedor(cnpj):
    fornecedores_dados = []
    try:
        with open("data/fornecedores.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 15 and partes[0] != cnpj:
                    fornecedores_dados.append(linha.strip())
    except FileNotFoundError:
        pass
    with open("data/fornecedores.txt", "w") as f:
        for fornecedor in fornecedores_dados:
            f.write(fornecedor + "\n")