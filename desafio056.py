# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

total_age = 0
media_age = 0
man_older = 0
name_older = ''
total_woman_20 = 0
for p in range (1,5):
    print(f'\033[31m______\033[m Dados da {p}ª pessoa \033[31m_____\033[m')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).upper()
    total_age += age
    if sex == 'M':
        if p == 1:
            man_older = age
            name_older = name
        if age > man_older:
            man_older = age
            name_older = name
    elif sex == 'F':
        if age < 20:
            total_woman_20 += 1
    else:
        print('Sexo inválido')
        exit(1)
media_age = total_age / 4
print(f'A média de idade das 4 pessoas é de {media_age} anos.')
print(f'O homem mais velho é o {name_older} de {man_older} anos.')
print(f'Existem {total_woman_20} mulheres menores de 20 anos.')
