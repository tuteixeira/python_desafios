# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(name='<desconhecido>', goal=0):
    print(f'{name} marcou {goal} gol(gols). ')
n = str(input('Digite o nome do jogador: ')).strip()
g = str(input(f'Total de gols {n} marcou: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(goal=g)  #Se n estiver fazio, passa apenas o parâmetro g
else:
    ficha(n, g)
