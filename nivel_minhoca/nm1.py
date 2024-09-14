def formatar_nome(nome):
    """
    Formata o nome completo, colocando a primeira letra de cada palavra em maiúscula e as demais em minúscula.

    Args:
        nome (str): O nome completo a ser formatado.

    Returns:
        str: O nome formatado, com cada palavra começando com letra maiúscula.
    """
    nome = nome.title()
    return nome

nome = input("Digite seu nome completo: ")
print(formatar_nome(nome))