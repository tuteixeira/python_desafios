#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

num = 0
count = soma = 0
while True:
    num = int(input('[USE 999 PARA PARAR] Digite um nº: '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'Você digitou {count} nº e a soma deu {soma}.')
