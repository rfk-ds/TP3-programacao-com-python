def substituir_palavra(frase, palavra_antiga, palavra_nova):
    """
    Substitui todas as ocorrências de uma palavra específica em uma frase por outra palavra fornecida.

    Args:
        frase (str): A frase onde as substituições serão realizadas.
        palavra_antiga (str): A palavra que será substituída.
        palavra_nova (str): A nova palavra que substituirá a palavra antiga.

    Returns:
        str: A frase resultante com todas as ocorrências da palavra antiga substituídas pela palavra nova.
    """
    frase = frase.replace(palavra_antiga, palavra_nova)
    return frase

frase = "Não deixe o samba morrer, não deixe o samba acabar, o morro foi feito de samba, de samba pra gente sambaaaaar"
palavra_antiga = "samba"
palavra_nova = input("Digite a palavra que deseja substituir: ")
print(substituir_palavra(frase, palavra_antiga, palavra_nova))