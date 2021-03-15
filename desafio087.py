# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A)A soma de todos os valores pares digitados.B) A soma dos valores da terceira coluna.C) O maior valor da segunda linha.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
countpair = allthirdcolumn = biggestsecondcolumn = 0

for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Digite o [{line},{column}] termo: '))


for index0, line in enumerate(matrix):
    if index0 == 1:
        biggestsecondcolumn = max(line)
    for index1, num in enumerate(line):
        if num % 2 == 0:
            countpair += num
        if index1 == 2:
            allthirdcolumn += num


print(f'Sua matriz é:\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}')
print(f'A soma de todos os elementos pares é: {countpair}')
print(f'A soma de todos os elementos da terceira coluna é: {allthirdcolumn}')
print(f'O maior elemento da segunda linha é: {biggestsecondcolumn}')