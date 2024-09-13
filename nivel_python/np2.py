def vendas_produtos(transacoes):
    """
    Processa uma lista de transações e retorna um dicionário com o total de vendas por produto.
    
    Args:
        transacoes (list): Lista de transações no formato 'id_produto,nome_produto,quantidade,valor_total'.
    
    Returns:
        dict: Dicionário com o id do produto como chave e um dicionário com o nome do produto, quantidade e valor total como valores.
    """
    vendas = {}
    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_total = transacao.split(',')
        quantidade = int(quantidade)
        valor_total = float(valor_total)

        if id_produto in vendas:
            vendas[id_produto]['quantidade'] += quantidade
            vendas[id_produto]['valor_total'] += valor_total
        else:
            vendas[id_produto] = {'nome_produto': nome_produto, 'quantidade': quantidade, 'valor_total': valor_total}
    
    return vendas

def produto_mais_vendido_e_maior_receita(vendas):
    """
    Retorna o produto mais vendido e o que gerou maior receita.
    
    Args:
        vendas (dict): Dicionário com os dados de vendas dos produtos.
    
    Returns:
        tuple: O nome do produto mais vendido e o nome do produto que gerou maior receita.
    """
    mais_vendido = max(vendas, key=lambda nome: vendas[nome]['quantidade'])
    maior_receita = max(vendas, key=lambda nome: vendas[nome]['valor_total'])
    
    return mais_vendido, maior_receita

def converter_valores(vendas, fator):
    """
    Converte o valor total das vendas para uma nova moeda, usando um fator de conversão.
    
    Args:
        vendas (dict): Dicionário com os dados de vendas dos produtos.
        fator (float): Fator de conversão para outra moeda.
    
    Returns:
        dict: Dicionário com os valores convertidos para a nova moeda.
    """
    vendas_convertidas = {}
    for nome_produto, dados in vendas.items():
        valor_convertido = dados['valor_total'] * fator
        vendas_convertidas[nome_produto] = {'quantidade': dados['quantidade'], 'valor_total': valor_convertido}
    
    return vendas_convertidas

def exibir_vendas(vendas):
    """
    Exibe as vendas de cada produto no formato 'id_produto: nome_produto - quantidade unidades - R$ valor_total'.
    
    Args:
        vendas (dict): Dicionário com os dados de vendas dos produtos.
    """
    for id_produto, dados in vendas.items():
        print(f'{id_produto}: {dados["nome_produto"]} - {dados["quantidade"]} unidades - R$ {dados["valor_total"]:.2f}')


def exibir_vendas_convertidas(vendas):
    """
    Exibe as vendas de cada produto em moeda convertida no formato 'produto: quantidade unidades - US$ valor_total'.
    
    Args:
        vendas (dict): Dicionário com os dados de vendas dos produtos.
    """
    for nome_produto, dados in vendas.items():
        print(f'{nome_produto}: {dados["quantidade"]} unidades - US$ {dados["valor_total"]:.2f}')

# Exemplo de uso
transacoes = [
    '1,Notebook,5,5000.00',
    '2,Smartphone,10,3000.00',
    '1,Notebook,3,3000.00',
    '3,Tablet,8,2000.00',
    '2,Smartphone,5,1500.00'
]

vendas = vendas_produtos(transacoes)
exibir_vendas(vendas)

mais_vendido, maior_receita = produto_mais_vendido_e_maior_receita(vendas)
print(f'\nProduto mais vendido: {mais_vendido}')
print(f'Produto que gerou maior receita: {maior_receita}')

fator = float(input('\nDigite o fator de conversão: '))
vendas_convertidas = converter_valores(vendas, fator)
exibir_vendas_convertidas(vendas_convertidas)
