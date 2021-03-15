# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.

big = 0
small = 0
num = list()
for pos in range(0, 5):
    num.append(int(input(f'Digite um nº para a posição {pos + 1}: ')))
    if pos == 0:
        big = num[pos]
        small = num[pos]
    else:
        if num[pos] > big:
            big = num[pos]
        if num[pos] < small:
            small = num[pos]
print(f'Sua lista é: {num}')
print(f'O maior valor é {big} na/nas posição/posições: - ', end=' ')
for i, v in enumerate(num):
    if v == big:
        print(f'{i+1} - ', end='')
print(f'\nO menor valor é {small} na/nas posição/posições: - ', end=' ')
for i, v in enumerate(num):
    if v == small:
        print(f'{i+1} -', end='')
