# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

name_weight = list()
data = list()
lighter_list = list()
heaviest_list = list()
keep = ''
counter = lighter = heaviest = 0

while True:
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso: ')))
    counter += 1
    if counter == 1:
        lighter = heaviest = data[1]
        heaviest_list.append(data[0])
        lighter_list.append(data[0])
    else:
        if data[1] == heaviest:
            heaviest_list.append(data[0])
        if data[1] == lighter:
            lighter_list.append(data[0])
        if data[1] > heaviest:
            heaviest = data[1]
            heaviest_list = list()
            heaviest_list.append(data[0])
        elif data[1] < lighter:
            lighter = data[1]
            lighter_list = list()
            lighter_list.append(data[0])
    name_weight.append(data[:])
    data.clear()
    keep = str(input('Continua? [ S/N ] ')).strip().upper()[0]
    while keep not in 'NS':
        keep = str(input('Digite: -S ou N- ')).strip().upper()[0]
    if keep == 'N':
        break

print(f'Foram cadastradas {len(name_weight)} pessoa(as)')
print(f'A(as) pessoa(as) mais pesada(as) foi(foram): {heaviest_list} com {heaviest} kilos e a(as) pessoa(as) mais leve(es) foi(foram): {lighter_list} com {lighter} Kilos.')
