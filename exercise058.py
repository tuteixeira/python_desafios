# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tries = 1
num = randint(0,10)
value = int(input('Tente descobrir o nº que eu pensei: '))
while value != num:
    if value > num:
        value = int(input('Menos, tente de novo: '))
    else:
        value = int(input('Mais, tente de novo: '))
    tries += 1
print(f'Sucesso! Eu escolhi {num} e vc tentou {tries} vezes.')
