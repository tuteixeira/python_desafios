#Exercício Python 018: Faça um algoritmo que leia um ângulo qualquer e mostre na tela o valor do seno, cesseno e tangente desse ângulo.

import math

ang = float(input('Diga um ângulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f' O ângulo {ang} possui: Seno = {sin:.1f}, Coseno = {cos:.1f} e a Tangente = {tan:.1f}. ')
