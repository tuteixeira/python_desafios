#  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
#  na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('~' *50)
print(f'{"Listagem de Compras" :^50}')
print('~' *50)
list = ('Saia', '19.90',
     'Blusa', '9.90',
     'Tênis', '99.90',
     'Casaco', '99.00',
     'Meias', '15.00',
     'Mochila', '49.00',
     'Calcinhas', '29.00',
     'Cuecas', '29.00')
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<20}', end=' ')
    else:
        print(f'R$ {list[pos]:>6}')
print('~' *50)
