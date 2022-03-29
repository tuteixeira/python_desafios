# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

player = dict()
goals = list()
name = str(input('Nome do jogador: '))
games = int(input(f'Quantas partidas {name} jogou? '))
player.update({'nome': name, 'partidas': games})
for c in range(0, games):
    goal = int(input(f'Quantos gols {name} marcou na partida {c+1}: '))
    goals.append(goal)
player['gols'] = goals
player['total_gols'] = sum(goals)
print(f'~' * 30)
print(player)
print(f'~' * 30)
for k, v in player.items():
    print(f'{k} tem valor {v}')
print(f'~' * 30)
print(f'O jogador {player["nome"]} jogou {player["partidas"]} partidas:')
for c in range(0, player['partidas']):
    print(f'Na partida {c+1} {player["nome"]} marcou {player["gols"][c]} gol/gols.')
print(f'{player["nome"]} fez um total de {player["total_gols"]} gols')
