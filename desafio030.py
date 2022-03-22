#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um nº: '))
r = n % 2
if r == 0:
    print(f'O nº {n} é par.')
else:
    print(f'O nº {n} é ímpar.')
