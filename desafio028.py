#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
print('Olá, vou escolher um número entre 0 e 5 e vc tenta acertar, ok?')
n = random.randint(0,5)
escolha = int(input('Diz aí, q nº achas q eu vou escolher: '))
print('Processando ... ')
time.sleep(2)
print('Escolhi o nº {}.' .format(n))
if escolha == n:
    print('Então tu acertou, sabe mto')
else:
    print('Então tu errou seu miserável')
