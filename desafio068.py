#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

answer = ' '
count = 0
while True:
    num = int(input('Qual nº vc escolhe? '))
    answer = str(input('Quer PAR ou ÍMPAR? ')) .strip() .upper()[0]
    com = randint(0,10)
    sum = num + com
    while answer not in 'PI':
        answer = str(input('Quer PAR ou ÍMPAR? ')).strip().upper()[0]
    if sum % 2 == 0:
        if answer == 'P':
            print(f'Ganhou, {num} + {com} é {sum} que é par')
            count += 1
        else:
            print(f'Perdeu, {num} + {com} é {sum} que é par')
            break
    else:
        if answer == 'I':
            print(f'Ganhou, {num} + {com} é {sum} que é ímpar')
            count += 1
        else:
            print(f'Perdeu, {num} + {com} é {sum} que é ímpar')
            break
print(f'GAME OVER vc venceu {count} vezes. ' if count != 0 else ' GAME OVER TU NUNCA GANHOU')
