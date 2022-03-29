# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

list = [[], []]

for v in range(0, 7):
    value = int(input(f'Digite o {v+1}º valor: '))
    if value % 2 == 0:
        list[0].append(value)
        list[0].sort()
    else:
        list[1].append(value)
        list[1].sort()

print(f'Os valores pares digitados são: {list[0]} \nOs ímpares são: {list[1]}')
