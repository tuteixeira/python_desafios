# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


def ajuda(com):
    title(f'Acessando o manuel de {com}: ')
    help(com)


def title(msg):
    tam = len(msg)
    print(f'\033[1;31m~\033[m' * tam)
    print(f'{msg}')
    print(f'\033[1;31m~\033[m' * tam)


command = ''
while True:
    title('Sistema de Ajuda PyHelp')
    command = str(input('Função ou biblioteca > '))
    if command.upper() == 'FIM':
        break
    else:
        ajuda(command)
title('Volte sempre')