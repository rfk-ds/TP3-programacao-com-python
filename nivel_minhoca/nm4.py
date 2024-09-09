# Desenvolva um programa que solicite ao usuário uma frase e imprima o número de caracteres, de palavras e de espaços em branco nesta frase.

def contar_caracteres_palavras_espacos(frase):
    caracteres = len(frase)
    palavras = len(frase.split())
    espacos = frase.count(" ")
    return caracteres, palavras, espacos

frase = input("Digite uma frase: ")
caracteres, palavras, espacos = contar_caracteres_palavras_espacos(frase)
print(f"A frase possui {caracteres} caracteres, {palavras} palavras e {espacos} espaços em branco.")
