# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

player = dict()
gols = list()


nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? '))
player.update({'nome': nome, 'partidas': partidas})
for c in range(0, partidas):
    gol = int(input(f'Quantos gols {nome} marcou na partida {c+1}: '))
    gols.append(gol)
player['gols'] = gols
player['totalgols'] = sum(gols)
print(f'~' * 30)
print(player)
print(f'~' * 30)
for k, v in player.items():
    print(f'{k} tem valor {v}')
print(f'~' * 30)
print(f'O jogador {player["nome"]} jogou {player["partidas"]} partidas:')
for c in range(0, player['partidas']):
    print(f'Na partida {c+1} {player["nome"]} marcou {player["gols"][c]} gol/gols.')
print(f'{player["nome"]} fez um total de {player["totalgols"]} gols')
