#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JÚNIOR, Até 25 anos: SÊNIOR, Acima de 25 anos: MASTER.

from datetime import date

date_today = date.today().year
registry = int(input('Atleta, digite sua matrícula para a verificação de sua categoria: '))
approve_registry = str(input(f'Sua matícula é {registry}, confirma? Digite S para SIM ou N para NÂO: ')).upper()
if approve_registry == 'N':
    print('Tente novamente:')
    exit(1)
else:
    year_birth = int(input('Para saber sua categoria, digite o ano de seu nascimento - \033[1;30;41mFORMATO 1900\033[m : '))
age = date_today - year_birth
if age <= 9:
    print('Sua categoria é: \033[31mMIRIM\033[m')
elif age <= 14:
    print('Sua categoria é: \033[31mINFANTIL\033[m')
elif age <= 19:
    print('Sua categoria é: \033[31mJÚNIOR\033[m')
elif age <= 25:
    print('Sua categoria é: \033[31mSÊNIOR\033[m')
else:
    print('Sua categoria é: \033[31mMASTER\033[m')