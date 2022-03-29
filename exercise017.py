#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

'''co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print(f' A soma do quadrado de {co} e {ca} vale {hip :.3f}. ')'''

import math

co = float(input(' Qual o cateto oposto? '))
ca = float(input( 'Qual o cateto adjacente? '))
hip = math.hypot(co, ca)
print(f'O valor da hipotenusa vale {hip:.3f}')
