# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

nameweight = list()
data = list()
lighterlist = list()
heaviestlist = list()
continuar = ''
counter = lighter = heaviest = 0

while True:
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso: ')))
    counter += 1
    if counter == 1:
        lighter = heaviest = data[1]
        heaviestlist.append(data[0])
        lighterlist.append(data[0])
    else:
        if data[1] == heaviest:
            heaviestlist.append(data[0])
        if data[1] == lighter:
            lighterlist.append(data[0])
        if data[1] > heaviest:
            heaviest = data[1]
            heaviestlist = list()
            heaviestlist.append(data[0])
        elif data[1] < lighter:
            lighter = data[1]
            lighterlist = list()
            lighterlist.append(data[0])

    nameweight.append(data[:])
    data.clear()
    continua = str(input('Continua? [ S/N ] ')).strip().upper()[0]
    while continua not in 'NS':
        continua = str(input('Digite: -S ou N- ')).strip().upper()[0]
    if continua == 'N':
        break

print(f'Foram cadastradas {len(nameweight)} pessoa(as)')
print(f'A(as) pessoa(as) mais pesada(as) foi(foram): {heaviestlist} com {heaviest} kilos e a(as) pessoa(as) mais leve(es) foi(foram): {lighterlist} com {lighter} Kilos.')
