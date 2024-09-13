"""
Uma empresa de comércio eletrônico deseja analisar os dados de vendas para entender melhor o comportamento dos clientes e otimizar as estratégias de marketing.

Implemente um programa em Python que receba uma lista de transações, onde cada transação é representada por uma string no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Total". O programa deve calcular e exibir o valor total das vendas para cada produto.

Crie uma função que receba a lista de transações e retorne o produto mais vendido (baseado na quantidade) e o produto que gerou a maior receita total.

Escreva um script que converta os valores totais de vendas para uma nova moeda, dado um fator de conversão fornecido pelo usuário. Exiba os valores convertidos no formato monetário adequado.
"""

def calcular_vendas(transacoes):
    vendas_por_produto = {}
    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_total = transacao.split(",")
        if nome_produto not in vendas_por_produto:
            vendas_por_produto[nome_produto] = {"quantidade": 0, "valor_total": 0}
        vendas_por_produto[nome_produto]["quantidade"] += int(quantidade)
        vendas_por_produto[nome_produto]["valor_total"] += float(valor_total)
    return vendas_por_produto

def produto_mais_vendido_e_maior_receita(vendas_por_produto):
    produto_mais_vendido = max(vendas_por_produto, key=lambda produto: vendas_por_produto[produto]["quantidade"])
    produto_maior_receita = max(vendas_por_produto, key=lambda produto: vendas_por_produto[produto]["valor_total"])
    return produto_mais_vendido, produto_maior_receita

def converter_valores(transacoes, fator_conversao):
    transacoes_convertidas = []
    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_total = transacao.split(",")
        valor_convertido = float(valor_total) * fator_conversao
        transacao_convertida = f"{id_produto},{nome_produto},{quantidade},{valor_convertido:.2f}"
        transacoes_convertidas.append(transacao_convertida)
    return transacoes_convertidas


transacoes = []
while True:
    transacao = input("Digite a transação (ou 'sair' para finalizar): ")
    if transacao.lower() == "sair":
        break
    transacoes.append(transacao)

vendas_por_produto = calcular_vendas(transacoes)
produto_mais_vendido, produto_maior_receita = produto_mais_vendido_e_maior_receita(vendas_por_produto)

print("Vendas por produto:")
for produto, vendas in vendas_por_produto.items():
    print(f"{produto}: {vendas['quantidade']} unidades - R$ {vendas['valor_total']:.2f}")

print(f"Produto mais vendido: {produto_mais_vendido}")
print(f"Produto com maior receita: {produto_maior_receita}")

fator_conversao = float(input("Digite o fator de conversão: "))
transacoes_convertidas = converter_valores(transacoes, fator_conversao)

