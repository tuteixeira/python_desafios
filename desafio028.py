#Exercício Python 028:Escreva um programa que faça o computador escolher um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
print('Olá, vou escolher um número entre 0 e 5 e vc tenta acertar, ok?')
n = random.randint(0,5)
print('Processando ... ')
time.sleep(2)
escolha = int(input('Qual número você acha que eu escolhi? '))
print('Processando ... ')
time.sleep(2)
print(f'Escolhi o nº {n}.')
if escolha == n:
    print('Você acertou!')
else:
    print('Você errou!')
