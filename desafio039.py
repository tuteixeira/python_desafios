#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
print('Olá, estamos em {} e precisamos saber a sua situação com o exército brasileiro.' .format(atual))
sexo = str(input('Primeiramente, qual seu sexo? \033[4mUse \033[m\033[4;33mM \033[m\033[4mpara Mulher ou \033[m\033[4;33mH\033[m\033[4m para Homem\033[m: '))
sexo = sexo.upper()
if sexo == 'M':
    print('O serviço militar não é obrigatório para mulheres.')
    exit(1)
else:
    ano = int(input('Você deve informar o ano de seu nascimento. \033[1;30;44m[FORMATO 1900]\033[m : '))
idade = atual - ano
falta = abs(18 - idade)
anoexato = ano + 18
if idade > 18:
    print('Já passou {} anos do tempo que você deveria ter se alistado.'.format(falta), end='')
    print(' Seu alistamento foi em {}.'.format(anoexato))
elif idade < 18:
    print('Você ainda é muito jovem, faltam {} anos para seu alistamento.'.format(falta), end='')
    print(' Seu alistamento será no ano de {}.'.format(anoexato))
else:
    print('Você está na idade ideal para se alistar.')