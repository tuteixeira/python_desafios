#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Digite um nº: '))
c = n
f = 1
while c > 0:
    print(c,end='')
    print(' x ' if c != 1 else ' = ',end='')
    f *= c
    c -= 1
print(f)
