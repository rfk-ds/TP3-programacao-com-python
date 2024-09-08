# Crie um programa que solicite um nome completo ao usuário e formate-o de forma que todas as palavras comecem com letra maiúscula e o restante seja minúsculo e exiba-o na tela.

def formatar_nome(nome):
    nome = nome.title()
    return nome

nome = input("Digite seu nome completo: ")
print(formatar_nome(nome))