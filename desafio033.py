#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


print('Oi, preciso de sua ajuda:')
a = int(input('Digite um nº: '))
b = int(input('Digite outro: '))
c = int(input('É o último, prometo ... digite mais um nº: '))
lista = [a, b, c]
ordem = sorted(lista)
print('O maior nº é {} e o menor é {}.' .format(ordem[2], ordem[0]))

