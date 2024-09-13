import random
import string

def gerar_senha():
    """
    Gera uma senha aleatória segura.
    
    Returns:
        str: Senha gerada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choices(caracteres, k=8))
    
    return senha

def verificar_senha(senha):
    """
    Verifica se a senha atende aos critérios de segurança.
    
    Args:
        senha (str): Senha a ser verificada.
    
    Returns:
        str: Senha segura.
    """
    while len(senha) < 8 or not any(c.isupper() for c in senha) or not any(c.islower() for c in senha) or not any(c.isdigit() for c in senha) or not any(c in string.punctuation for c in senha):
        print('A senha deve ter no mínimo 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais.')
        senha = input('Digite uma nova senha: ')
    
    return senha

def criptografar_senhas(senhas):
    """
    Criptografa uma lista de senhas utilizando uma cifra de substituição.
    
    Args:
        senhas (list): Lista de senhas a serem criptografadas.
    
    Returns:
        list: Lista de senhas criptografadas.
    """
    alfabeto = string.printable
    chave = alfabeto[3:] + alfabeto[:3]
    senhas_criptografadas = []
    
    for senha in senhas:
        senha_criptografada = ''.join(chave[alfabeto.index(c)] if c in alfabeto else c for c in senha)
        senhas_criptografadas.append(senha_criptografada)
    
    return senhas_criptografadas

def descriptografar_senhas(senhas_criptografadas):
    """
    Descriptografa uma lista de senhas criptografadas utilizando uma cifra de substituição.
    
    Args:
        senhas_criptografadas (list): Lista de senhas criptografadas.
    
    Returns:
        list: Lista de senhas descriptografadas.
    """
    alfabeto = string.printable
    chave = alfabeto[3:] + alfabeto[:3]
    senhas = []
    
    for senha_criptografada in senhas_criptografadas:
        senha = ''.join(alfabeto[chave.index(c)] if c in chave else c for c in senha_criptografada)
        senhas.append(senha)
    
    return senhas

senhas = ['abc123', 'senha123', 'teste123']
senhas_criptografadas = criptografar_senhas(senhas)
senhas_descriptografadas = descriptografar_senhas(senhas_criptografadas)

print('Senhas:', senhas)
print('Senhas criptografadas:', senhas_criptografadas)
print('Senhas descriptografadas:', senhas_descriptografadas)
