# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

totalage = 0
mediaage = 0
manolder = 0
nameolder = ''
totalwoman20 = 0
for p in range (1,5):
    print('\033[31m______\033[m Dados da {}ª pessoa \033[31m_____\033[m' .format(p))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).upper()
    totalage += age
    if sex == 'M':
        if p == 1:
            manolder = age
            nameolder = name
        if age > manolder:
            manolder = age
            nameolder = name
    elif sex == 'F':
        if age < 20:
            totalwoman20 += 1
    else:
        print('Sexo inválido')
        exit(1)
mediaage = totalage / 4
print('A média de idade das 4 pessoas é de {} anos.' .format(mediaage))
print('O homem mais velho é o {} de {} anos.' .format(nameolder, manolder))
print('Existem {} mulheres menores de 20 anos.' .format(totalwoman20))
