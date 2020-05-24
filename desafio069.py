# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.


count = countage = countman = countwoman20 = 0
while True:
    sex = str(input('[M/F] SEXO: ')) .strip() .upper()[0]
    while sex not in 'MF':
        sex = str(input('[M/F] SEXO: ')).strip().upper()[0]
    if sex == 'M':
        countman += 1
    age = int(input('IDADE: '))
    if age > 18:
        countage += 1
    if sex == 'F' and age < 20:
        countwoman20 += 1
    keep = str(input('[S/N] continuar? ')) .strip() .upper()[0]
    while keep not in 'SN':
        keep = str(input('[S/N] continuar? ')).strip().upper()[0]
    count += 1
    if keep == 'N':
        break
print(f'''Existem {count} cadastradas:
{countage} são maiores de 18;
{countman} são homens; {countwoman20} são mulheres menores de 20''')

