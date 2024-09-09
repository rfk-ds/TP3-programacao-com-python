# Crie um script em Python que substitua todas as ocorrências de uma palavra específica em uma frase por outra palavra fornecida pelo usuário. Utilize um texto de exemplo de sua preferência e escolha a palavra a ser substituída, mas a lógica precisa funcionar para outros casos.

def substituir_palavra(frase, palavra_antiga, palavra_nova):
    frase = frase.replace(palavra_antiga, palavra_nova)
    return frase

frase = "Não deixe o samba morrer, não deixe o samba acabar, o morro foi feito de samba, de samba pra gente sambaaaaar"
palavra_antiga = "samba"
palavra_nova = input("Digite a palavra que deseja substituir: ")
print(substituir_palavra(frase, palavra_antiga, palavra_nova))