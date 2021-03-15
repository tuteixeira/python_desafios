# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.

from random import randint

numeros = list()
lista_pares = list()


def sorteia():
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
    print(f'A lista gerada é: {numeros}')


def soma_par():
    for e in numeros:
        if e % 2 == 0:
            lista_pares.append(e)
    print(f'A soma dos pares é : {sum(lista_pares)}')


sorteia()
soma_par()