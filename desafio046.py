#Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

start = str(input('Para iniciar a explosão dos fogos de articício digite: \033[7;33m NOW \033[m ')).upper() .strip()
if start == 'NOW'.upper():
    print('Sua contagem começa agora:')
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('\033[7;32m F O G O S \033[m')
else:
    print('Quando estiver preparado, digite: \033[7;33m NOW \033[m ')


