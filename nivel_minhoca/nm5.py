# Calcular a soma dos dígitos em uma string numérica fornecida pelo usuário, verificando se todos os caracteres são de fato numéricos.

def somar_digitos(string):
    soma = 0
    for caracter in string:
        if caracter.isdigit():
            soma += int(caracter)
    return soma

string = input("Digite uma string numérica: ")
print(somar_digitos(string))