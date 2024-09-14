def contar_caracteres_palavras_espacos(frase):
    """
    Conta o número de caracteres, palavras e espaços em branco em uma frase.

    Args:
        frase (str): A frase cuja análise será feita.

    Returns:
        tuple: Uma tupla contendo:
            - caracteres (int): Número total de caracteres na frase, incluindo espaços.
            - palavras (int): Número de palavras na frase.
            - espacos (int): Número de espaços em branco na frase.
    """
    caracteres = len(frase)
    palavras = len(frase.split())
    espacos = frase.count(" ")
    return caracteres, palavras, espacos

frase = input("Digite uma frase: ")
caracteres, palavras, espacos = contar_caracteres_palavras_espacos(frase)
print(f"A frase possui {caracteres} caracteres, {palavras} palavras e {espacos} espaços em branco.")
