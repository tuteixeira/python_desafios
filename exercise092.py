# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

data = dict()
name = str(input('Nome do trabalhador: '))
year = int(input(f'Ano de nascimento de {name}: '))
age = datetime.date.today().year - year
ctps = int(input(f'Nº da CTPS de {name}: '))
data.update({'nome': name, 'idade': age, 'ctps': ctps})
if ctps != 0:
    year_contract = int(input('1º ano de contratação: '))
    retirement = (datetime.date.today().year - year_contract) + 35
    salary = float(input(f'Salário atual de R$ {name}: '))
    data.update({'aposentadoria': retirement, 'salário': salary})
print('~' * 15, 'Dados do trabalhador', '~' * 15)
for k, v in data.items():
    print(f'{k} -> {v} ')
