#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''co = float(input(' Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print(' A soma do quadrado de {} e {} vale {:.3f}. ' .format(co, ca, hip))'''
import math
co = float(input(' Qual o cateto oposto? '))
ca = float(input( 'Qual o cateto adjacente? '))
hip = math.hypot(co, ca)
print('O valor da hipotenusa vale {:.3f}.' .format(hip))


