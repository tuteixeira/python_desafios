#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando quem e menor, maior ou igual caso necessário

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
if n1 < n2:
    print(f'{n1} é menor que {n2}')
elif n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 == n2:
    print('Os números são iguais')
    