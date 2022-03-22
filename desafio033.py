#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Digite 3 valores para eu os analisar:')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
lista = [a, b, c]
ordem = sorted(lista)
print(f'O maior nº é {ordem[2]} e o menor é {ordem[0]}.')

