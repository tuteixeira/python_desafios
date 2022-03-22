#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

sum = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite um nº: '))
    if num % 2 == 0:
        sum += num
        count += 1
print(f'A soma de {count} númros pares é {sum}.')