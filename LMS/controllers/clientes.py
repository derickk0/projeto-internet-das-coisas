"""
Nome do arquivo: clientes.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

def adicionar_cliente(cnpjCpf, nome, observacoes, telefone, celular, email, logradouro, numero, bairro, cidade, uf, cep, complemento):
    with open("data/clientes.txt", "a") as f:
        f.write(f"{cnpjCpf},{nome},{observacoes},{telefone},{celular},{email},{logradouro},{numero},{bairro},{cidade},{uf},{cep},{complemento}\n")

def listar_clientes_dados():
    clientes = []
    try:
        with open("data/clientes.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 13:
                    clientes.append({
                        'cnpjCpf': partes[0],
                        'nome': partes[1],
                        'observacoes': partes[2],
                        'telefone': partes[3],
                        'celular': partes[4],
                        'email': partes[5],
                    })
    except FileNotFoundError:
        pass
    return clientes

def listar_clientes_endereco():
    clientes = []
    try:
        with open("data/clientes.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 13:
                    clientes.append({
                        'logradouro': partes[6],
                        'numero': partes[7],
                        'bairro': partes[8],
                        'cidade': partes[9],
                        'uf': partes[10],
                        'cep': partes[11],
                        'complemento': partes[12]
                    })
    except FileNotFoundError:
        pass
    return clientes

def excluir_cliente(cnpjCpf):
    clientes_dados = []
    try:
        with open("data/clientes.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 13 and partes[0] != cnpjCpf:
                    clientes_dados.append(linha.strip())
    except FileNotFoundError:
        pass
    with open("data/clientes.txt", "w") as f:
        for cliente in clientes_dados:
            f.write(cliente + "\n")


