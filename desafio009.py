#Faça um programa q leia um nº inteiro qualquer e mostre sua tabuada - Usando o formato .format()

nome = input('Qual seu nome? ')
n = int(input(f'Oi {nome}, escolha um número entre 1 e 9: '))
print(f'Boa escolha, a tabuada completa do nº {n} é: ')
print('_____________________________________')
print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}' . format(n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
print('_____________________________________')

