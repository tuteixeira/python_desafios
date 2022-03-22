#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o 1º segmento de reta: '))
b = float(input('Digite o 2º segmento de reta: '))
c = float(input('Digite o 3º segmento de reta: '))
if a + b >= c and b + c >= a and c + a >= b:
#if abs(a-b) < c < a + b:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo com esses valores.')
