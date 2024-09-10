"""
Mini Projeto 1: Validação e Formatação de Dados em um Sistema de Cadastro

Na vida de um desenvolvedor e analista de sistemas a validação de dados é uma etapa extremamente importante que previne diversas dificuldades posteriores à coleta dos dados.

Crie um programa com funções em Python para solicitar ao usuário que insira os dados listados abaixo e valide os seguintes campos de cadastro com as seguintes regras:
CPF: verifique se o CPF possui 11 dígitos e formate-o no padrão "xxx.xxx.xxx-xx".
E-mail: verifique se o e-mail possui um formato válido (com "@" e um domínio válido) e normalize-o para minúsculas. Caracteres alfanuméricos + ‘@’ + Caracteres alfanuméricos + ‘.’ + Caracteres alfabéticos
Telefone: remova caracteres não numéricos e converta o número de telefone para um número inteiro e em uma string formatada como (XX) XXXXX-XXXX ou (XX) XXXX-XXXX e exibindo o inteiro e a string formatada na tela.
"""

def validar_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:
        return "CPF inválido."
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def validar_email(email):
    if "@" not in email or "." not in email.split("@")[1]:
        return "E-mail inválido."
    return email.lower()

def validar_telefone(telefone):
    telefone = "".join([caracter for caracter in telefone if caracter.isdigit()])
    if len(telefone) == 10:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    elif len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return "Telefone inválido."

cpf = input("Digite o CPF: ")
email = input("Digite o e-mail: ")
telefone = input("Digite o telefone: ")

print(validar_cpf(cpf))
print(validar_email(email))
print(validar_telefone(telefone))