# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

dados = dict()

nome = str(input('Nome do trabalhador: '))
ano = int(input(f'Ano de nascimento de {nome}: '))
idade = datetime.date.today().year - ano
ctps = int(input(f'Nº da CTPS de {nome}: '))
dados.update({'nome': nome, 'idade': idade, 'ctps': ctps})
if ctps != 0:
    anocotrat = int(input('1º ano de contratação: '))
    aposentadoria = (datetime.date.today().year - anocotrat) + 35
    salario = float(input(f'Salário atual de R$ {nome}: '))
    dados.update({'aposentadoria': aposentadoria, 'salário': salario})

print('~' * 15, 'Dados do trabalhador', '~' * 15)
for k, v in dados.items():
    print(f'{k} -> {v} ')



