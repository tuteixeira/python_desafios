#Faça um programa q leia um nº inteiro qualquer e mostre sua tabuada
nome = input('Qual seu nome? ')
n = int(input('Oi {}, escolha um número entre 1 e 9: ' .format(nome)))
print('Boa escolha, o nº {} é o meu nº da sorte, eu sei a tabuada completa dele, se liga:' .format(n))
print('_____________________________________')
print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}' . format(n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
print('_____________________________________')

