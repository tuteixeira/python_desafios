#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um nº: '))
r = n % 2
if r == 0:
    print('O nº {} é par.' .format(n))
else:
    print('O nº {} é ímpar.' .format(n))
