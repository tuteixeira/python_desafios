# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Goiás.


teams = ('Flamengo', 'Internacional', 'São Paulo', 'Cruzeiro', 'Palmeiras', 'Avaí', ' Atlético MG', 'Grêmio', 'Goiás', 'Corinthias', 'Baurueri', 'Santos',
          'Vitória', ' Athletico PR', 'Botafogo', 'Fluminense', 'Coritiba', 'Santo André', 'Náutico', 'Sport')
print('Classificação do Brasileirão em 2009')
print(f'Os 5 primeiros times são: {teams[:4]} ')
print(f'Os últimos 4 colocados são: {-4:}')
print(sorted(teams))
print(f'O Goiás ficou em ')
