# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(l, c):
    area = l * c
    print(area)


a = float(input('Largura do terreno em metros: '))
b = float(input('Comprimento do terreno em metros: '))

area(a, b)
