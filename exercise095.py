# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

game_dict = dict()
game_final_list = list()
while True:
    name = str(input('Nome: '))
    total_games = int(input(f'Total de partidas que {name} jogadas: '))
    game_dict.update({'name': name, 'games': total_games})

    goals_list = list()
    for c in range(0, total_games):
        goal = int(input(f'Total de gols na partida {c+1}: '))
        goals_list.append(goal)
    game_dict.update({'goals': goals_list.copy()})
    total_goal = sum(goals_list)
    game_dict.update({'total_goals': total_goal})
    game_final_list.append(game_dict.copy())

    keep = str(input('Cadastrar mais jogadores? [ S/N ] ')).upper().strip()
    while keep not in 'SN':
        keep = str(input('Por favor, digite [ S/N ]: ')).upper().strip()
    if keep == 'N':
        break
print(f'~' * 15, 'Informações dos jogadores: ', '~' * 15)
print(f'Nº do jogador ~ Nome do jogador ~ Total de partidas jogadas')
for i, v in enumerate(game_final_list):
    print(f'{i:^15} ~ {v["name"]:^17} ~ {v["games"]:^10}')

while True:
    choice_player = int(input('Digite o nº do jogador para mais informações: [DIGITE 999 PARA ENCERRAR] '))
    if choice_player == 999:
        break
    if choice_player >= len(game_final_list):
        print('Número inválido')
    else:
        player = game_final_list[choice_player]
        print(f'{choice_player} é: {player["name"]}, que jogou {player["games"]} partidas e marcou {player["total_goals"]} gols. ')
        print(f'{player["goals"]}')
