# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

count = count_age = count_man = count_woman20 = 0
while True:
    sex = str(input('[M/F] SEXO: ')) .strip() .upper()[0]
    while sex not in 'MF':
        sex = str(input('[M/F] SEXO: ')).strip().upper()[0]
    if sex == 'M':
        count_man += 1
    age = int(input('IDADE: '))
    if age > 18:
        count_age += 1
    if sex == 'F' and age < 20:
        count_woman20 += 1
    keep = str(input('[S/N] continuar? ')) .strip() .upper()[0]
    while keep not in 'SN':
        keep = str(input('[S/N] continuar? ')).strip().upper()[0]
    count += 1
    if keep == 'N':
        break
print(f'''Existem {count} cadastradas:
{count_age} são maiores de 18;
{count_man} são homens; {count_woman20} são mulheres menores de 20''')

