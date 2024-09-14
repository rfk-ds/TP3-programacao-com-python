def palavra_mais_longa(texto):
    """
    Encontra e retorna a palavra mais longa em um texto. Remove pontuações como vírgulas,
    pontos finais, exclamações e interrogações antes de realizar a busca.

    Args:
        texto (str): O texto de entrada que pode conter pontuação e múltiplas palavras.

    Returns:
        str: A palavra mais longa encontrada no texto. Se houver palavras com o mesmo comprimento,
             retorna a primeira que aparece no texto.
    """
    texto = texto.replace(",", "")
    texto = texto.replace(".", "")
    texto = texto.replace("!", "")
    texto = texto.replace("?", "")
    texto = texto.split()
    palavra_mais_longa = ""
    for palavra in texto:
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra
    return palavra_mais_longa

texto = "Não deixe o samba morrer, não deixe o samba acabar, o morro foi feito de samba, de samba pra gente sambaaaaar"
print(palavra_mais_longa(texto))