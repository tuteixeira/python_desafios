# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

n = int(input('Digite um nº: '))
a = 0
b = 1
inicio = 2
print('0 > 1', end='')
while inicio < n:
    out = a + b
    a = b
    b = out
    inicio += 1
    print(' > {}'.format(out), end='')
