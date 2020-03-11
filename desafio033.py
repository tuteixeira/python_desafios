#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Oi, preciso de sua ajuda:')
a = int(input('Digite um nº: '))
b = int(input('Digite outro: '))
c = int(input('É o último, prometo ... digite mais um nº: '))
if a < b and a < c :
    print('{} é o menor valor.' .format(a))
else b < a and b < c :
    print('{} é o menor valor.' .format(b))

