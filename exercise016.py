#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

import math
num = float(input('Digite um número: '))
print(f'O número {num} possui {math.trunc(num)} como parte inteira. ')
'''from math import trunc
num = float(input('Digite um número: '))
print(f'O número {num} possui {trunc(num)} como parte inteira.')'''
