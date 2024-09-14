def calcular_expressao(expressao):
    """
    Avalia uma expressão matemática básica composta por números e operadores aritméticos (+, -, *, /).

    Args:
        expressao (str): A expressão matemática a ser avaliada. Deve conter apenas números e os operadores aritméticos.

    Returns:
        float or str: O resultado da expressão se for válida. Caso contrário, retorna 'Expressão inválida.'.
    """
    for caracter in expressao:
        if caracter not in "1234567890+-*/":
            return "Expressão inválida."
    return eval(expressao)

expressao = input("Digite uma expressão matemática básica: ")
print(calcular_expressao(expressao))