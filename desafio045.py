# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ['PEDRA', 'PAPEL', 'TESOURA']
pc = randint(0,2)
print(""" Bora jogar seu lixo humano.
É muito fácil jogar, basta escolher uma das opções abaixo:
Digite \033[1;34m0\033[m para \033[1;34mPEDRA\033[m
Digite \033[1;34m1\033[m para \033[1;34mPAPEL\033[m
Digite \033[1;34m2\033[m para \033[1;34mTESOURA\033[m """)
human = int(input('Qual nº vc escolhe? '))
if human != 0 and human != 1 and human != 2:
    print('\033[1;31mCOMANDO INVÁLIDO\033[m')
    exit(1)
else:
    print('Eu joguei {}' .format(itens[pc]) ,end='')
    print(' e você jogou {}.' .format(itens[human]))
if pc == 0 and human == 1:
    print('Vc ganhou!')
elif pc == 0 and human == 2:
    print('Eu ganhei!')
elif human == 0 and pc == 1:
    print('Eu ganhei!')
elif human == 0 and pc == 2:
    print('Vc ganhou!')
elif pc == 1 and human == 2:
    print('Vc ganhou!')
elif human == 2 and pc == 1:
    print('Eu ganhei!')
elif pc == human:
    print('Nós empatamos!')
