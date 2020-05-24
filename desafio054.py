# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

yeartoday = date.today().year
younger = 0
older = 0
olderYears = []
youngerYear = []
for c in range(1, 4):
    year = int(input('Digite o ano de nascimento: '))
    age = yeartoday - year
    if age >= 18:
        older += 1
        olderYears.append(year)
    else:
        younger += 1
        youngerYear.append(year)
print('Existem {} maiores que são os nascidos em {} e {} menores que são os nascidos em {}.' .format(older, olderYears, younger, youngerYear))

