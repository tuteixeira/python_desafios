#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""" a = int(input("Digite um nº: "))
b = int(input("Digite outro nº: "))
c = int(input("Pra terminar, digite mais um nº: "))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor é {}\nE o maior valor é {}. " .format(menor, maior)) """

a = int(input('Digite um nº: '))
b = int(input('Digite mais um nº: '))
c = int(input('Digite o último nº: '))
a == b and b == c
print('Os nº são iguais')
num = [a, b, c]
print('O maior valor é {} \nO menor valor é {}. ' .format(max(num), min(num)))