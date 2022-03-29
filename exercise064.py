#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = sum = count = 0
while n != 999:
    n = int(input('[USE 999 PARA PARAR] Digite um nº : '))
    if n != 999:
        count += 1
        sum += n
print(f'Você digitiu {count} º e a soma de todos eles é {sum}.')
