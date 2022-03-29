# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
import time

name = str(input('Olá, qual seu nome? '))
data = list()
how_many_times = int(input(f'Quantos jogos você quer {name} ? '))
print(f'Vou torcer para você {name} ! Boa sorte \033[32m ~🍀~\033[m ')
#while total <= howmanytimes:
for c in range(0, how_many_times):
    count = 0
    while count < 6:
        num = random.randint(1, 60)
        if num not in data:
            data.append(num)
            count += 1
    data.sort()
    print(f'Jogo {c+1} : {data}')
    time.sleep(1)
    data.clear()
