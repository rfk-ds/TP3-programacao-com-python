def validar_cpf(cpf):
    """
    Valida e formata um número de CPF (Cadastro de Pessoa Física) brasileiro.

    Args:
        cpf (str): O número de CPF a ser validado. Deve conter 11 dígitos.

    Returns:
        str: Retorna o CPF formatado como 'XXX.XXX.XXX-XX' se válido.
             Caso contrário, retorna 'CPF inválido.'.
    """
    if not cpf.isdigit() or len(cpf) != 11:
        return "CPF inválido."
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def validar_email(email):
    """
    Valida e formata um endereço de e-mail.

    Args:
        email (str): O endereço de e-mail a ser validado.

    Returns:
        str: Retorna o e-mail em letras minúsculas se for válido.
             Caso contrário, retorna 'E-mail inválido.'.
    """
    if "@" not in email or "." not in email.split("@")[1]:
        return "E-mail inválido."
    return email.lower()

def validar_telefone(telefone):
    """
    Valida e formata um número de telefone brasileiro.

    Args:
        telefone (str): O número de telefone a ser validado. Pode conter 10 ou 11 dígitos.

    Returns:
        str: Retorna o telefone formatado como '(XX) XXXX-XXXX' ou '(XX) XXXXX-XXXX'.
             Caso contrário, retorna 'Telefone inválido.'.
    """
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