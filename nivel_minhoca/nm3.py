# Escreva uma função que receba um texto e retorne a palavra mais longa presente nele, desconsiderando pontuação.

def palavra_mais_longa(texto):
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
