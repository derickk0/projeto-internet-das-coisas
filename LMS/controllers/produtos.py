"""
Nome do arquivo: produtos.py
Equipe: Erick Breno Pereira, Arthur Nascimento, Guilherme Moura, Andrei Luiz
Turma: G91164
Semestre: 2025.1
"""

def adicionar_produto(codigo, fornecedor, nome, descricao, tipo, quantidade, validade, observacoes):
    with open("data/produtos.txt", "a") as f:
        f.write(f"{codigo},{fornecedor},{nome},{descricao},{tipo},{quantidade},{validade},{observacoes}\n")

def listar_produtos():
    produtos = []
    try:
        with open("data/produtos.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 8:
                    produtos.append({
                        'codigo': partes[0],
                        'fornecedor': partes[1],
                        'nome': partes[2],
                        'descricao': partes[3],
                        'tipo': partes[4],
                        'quantidade': partes[5],
                        'validade': partes[6],
                        'observacoes': partes[7]
                    })
    except FileNotFoundError:
        pass
    return produtos

def excluir_produto(codigo):
    produtos = []
    try:
        with open("data/produtos.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 8 and partes[0] != codigo:
                    produtos.append(linha.strip())
    except FileNotFoundError:
        pass
    
    with open("data/produtos.txt", "w") as f:
        for produto in produtos:
            f.write(produto + "\n")