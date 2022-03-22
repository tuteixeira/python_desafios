#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou se passou do prazo.

from datetime import date

atual = date.today().year
print(f'Olá, estamos em {atual} e precisamos saber a sua situação com o exército brasileiro.')
sexo = str(input('Primeiramente, qual seu sexo? \033[mUse \033[m\033[33mM \033[m\033[4mpara Mulher ou \033[m\033[4;33mH\033[m\033[4m para Homem\033[m: '))
sexo = sexo.upper()
if sexo == 'M':
    print('O serviço militar não é obrigatório para mulheres.')
    exit(1)
else:
    ano = int(input('Você deve informar o ano de seu nascimento. \033[1;30;44m[FORMATO 1900]\033[m : '))
idade = atual - ano
falta = abs(18 - idade)
ano_exato = ano + 18
if idade > 18:
    print(f'Já passou {falta} anos do tempo que você deveria ter se alistado.', end='')
    print(f' Seu alistamento foi em {ano_exato}.')
elif idade < 18:
    print(f'Você ainda é muito jovem, faltam {falta} anos para seu alistamento.', end='')
    print(f' Seu alistamento será no ano de {ano_exato}.')
else:
    print('Você está na idade ideal para se alistar.')