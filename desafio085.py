# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


lista = [[], []]

for v in range(0, 7):
    valor = int(input(f'Digite o {v+1}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
        lista[0].sort()
    else:
        lista[1].append(valor)
        lista[1].sort()

print(f'Os valores pares digitados são: {lista[0]} \nOs ímpares são: {lista[1]}')
