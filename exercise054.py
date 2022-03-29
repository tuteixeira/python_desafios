# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

year_today = date.today().year
younger = 0
older = 0
older_years = []
younger_year = []
for c in range(1, 8):
    year = int(input('Digite o ano de nascimento: '))
    age = year_today - year
    if age >= 18:
        older += 1
        older_years.append(year)
    else:
        younger += 1
        younger_year.append(year)
print(f'Existem {older} maiores que são os nascidos em {older_years} e {younger} menores que são os nascidos em {younger_year}.')
