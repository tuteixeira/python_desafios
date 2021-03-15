# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial


def fatorial(n, show=False):
    """
    - Calcula o fatorial de um número
    :param n: Número a ser calculado
    :param show: opicional mostrar ou não a conta
    :return: fatorial de n
    by Tuíra
    """
    fac = 1  # Fator nulo da multiplicação é 1
    for count in range(factorial, 0, -1):
        fac = fac * count
        if show:
            print(count, end=' - ')

    return f'\033[1;31m {fac} \033[m'


factorial = int(input('Digite um nº: '))
print(fatorial(factorial, show=True))
help(fatorial)


