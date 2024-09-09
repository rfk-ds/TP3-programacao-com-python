# Calcular o resultado de uma expressão matemática básica fornecida como string pelo usuário, ignorando espaços, permitindo apenas caracteres numéricos e os operadores +, -, * e /.

def calcular_expressao(expressao):
    for caracter in expressao:
        if caracter not in "1234567890+-*/":
            return "Expressão inválida."
    return eval(expressao)

expressao = input("Digite uma expressão matemática básica: ")
print(calcular_expressao(expressao))