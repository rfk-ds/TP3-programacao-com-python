def somar_digitos(string):
    """
    Soma todos os dígitos numéricos presentes em uma string.

    Args:
        string (str): A string que pode conter dígitos e outros caracteres.

    Returns:
        int: A soma de todos os dígitos encontrados na string.
             Se a string não contiver dígitos, retorna 0.
    """
    soma = 0
    for caracter in string:
        if caracter.isdigit():
            soma += int(caracter)
    return soma

string = input("Digite uma string numérica: ")
print(somar_digitos(string))