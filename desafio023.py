#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = int(input('Digite um nº entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando esse nº, eu sei que:')
print('Sua unidade: {}' .format(u))
print('Sua dezena: {}' .format(d))
print('Sua centena: {}' .format(c))
print('Seu milhar: {}' .format(m))
