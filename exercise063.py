# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

n = int(input('Digite um nº: '))
a = 0
b = 1
start = 2
print('0 > 1', end='')
while start < n:
    out = a + b
    a = b
    b = out
    start += 1
    print(f' > {out}', end='')
