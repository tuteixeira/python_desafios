# #Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. USANDO FOR

n = int(input('Digite um nº: '))
c = n
f = 1
for c in range(c, 0, -1):
    print(c, end=' x ' if c != 1 else ' = ')
    f *= c
print(f)