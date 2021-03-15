# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matrix = [[], [], []]

for c in range(1, 10):
    num = int(input(f'Digite o {c}º termo: '))
    if c <= 3:
        matrix[0].append(num)
    elif 3 < c <= 6:
        matrix[1].append(num)
    else:
        matrix[2].append(num)

print(f'Sua matriz é:\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}')
