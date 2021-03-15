# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


from random import randint

ranking = list()
game = dict()
for c in range(0, 4):
    name = str(input(f'Nome do jogador {c+1}: '))
    dice = randint(1, 6)
    game['gamer ' + str(c+1)] = {'nome': name, 'dado': dice}


for k, v in game.items():
    print(f'{k} -> {v["nome"]} tirou {v["dado"]} no dado.')

ranking = sorted(game.items(), key=lambda x: x[1]['dado'], reverse=True)

position = 1
dado = 0
for i, v in enumerate(ranking):
    if dado > v[1]["dado"]:
        position = i+1
    print(f'Em {position}º -> Jogador {v[1]["nome"]} com {v[1]["dado"]} no dado.')
    dado = v[1]["dado"]

