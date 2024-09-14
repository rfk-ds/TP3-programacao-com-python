"""
Um escritório de advocacia deseja automatizar parte do processo de análise de contratos, extraindo informações relevantes de documentos longos.

Desenvolva um programa que receba o texto completo de um contrato e extraia todas as cláusulas que mencionem valores monetários. Os valores devem ser identificados e exibidos em uma lista separada.

Implemente uma função que, dada uma lista de termos legais, verifique quantas vezes cada termo aparece no contrato e exiba as ocorrências em ordem decrescente de frequência.
"""

import re

def extrair_valores_monetarios(contrato):
    valores_monetarios = re.findall(r'R\$\s?\d+(?:\.\d{3})*(?:,\d+)?', contrato)
    
    return valores_monetarios

def extrair_termos_legais(contrato, termos_legais):
   
    contagem_termos = {termo: contrato.lower().count(termo.lower()) for termo in termos_legais}
    contagem_termos = {termo: contagem for termo, contagem in sorted(contagem_termos.items(), key=lambda item: item[1], reverse=True)}
    
    return contagem_termos

contrato = """
Contrato de Prestação de Serviços

Cláusula 1ª - O contratante pagará ao contratado o valor de R$ 1.500,00 (mil e quinhentos reais) mensais.

Cláusula 2ª - O contratado se compromete a prestar os serviços descritos no anexo I deste contrato.

Cláusula 3ª - O presente contrato terá vigência de 12 (doze) meses, a contar da data de assinatura.

Cláusula 4ª - O contratante poderá rescindir o contrato a qualquer momento, mediante aviso prévio de 30 (trinta) dias.

Cláusula 5ª - O contratado não poderá prestar serviços a terceiros durante a vigência deste contrato.

Cláusula 6ª - Este contrato poderá ser prorrogado por mais 12 (doze) meses, mediante acordo entre as partes.

"""

valores_monetarios = extrair_valores_monetarios(contrato)
print(valores_monetarios)


termos_legais = ['cláusula', 'contratante', 'contratada', 'vigência', 'rescisão', 'prorrogação']
contagem_termos = extrair_termos_legais(contrato, termos_legais)

for termo, contagem in contagem_termos.items():
    print(f'{termo}: {contagem}')