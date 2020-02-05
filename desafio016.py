#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
'''import math
num = float(input('Digite um número: '))
print('O nº {} possui {} como parte inteira. '.format(num, math.trunc(num)))'''
from math import trunc
num = float(input('Digite um número: '))
print('O número {} possui {} como parte inteira.' .format(num, trunc(num)))


