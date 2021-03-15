# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média


person = dict()
people = list()
women_list = list()
women_str = ''
people_older = list()
people_older_str = ''
continuar = ' '

while continuar != 'N':
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    sex = str(input('Sexo: [ M/F ] ')).strip().upper()
    while sex not in 'MF':
        sex = str(input('DIGITE [ M/F ] ')).strip().upper()
    person.update({'nome': name, 'idade': age, 'sexo': sex})
    people.append(person.copy())
    continuar = str(input('Continuar cadastrando? [ S/N ] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Digite: [ S/N ] ')).strip().upper()
        if continuar == 'N':
            break
total_age = total_older = 0
for i, p in enumerate(people):
    total_age += p['idade']
    if p['sexo'] == 'F':
        women_list.append(p['nome'])
        women_str += p['nome'] + ', '  # fiz uma lista de str para no print conseguir colocar ',' entre os nomes
age_average = total_age / len(people)
for i, p in enumerate(people):
    if p['idade'] > age_average:
        people_older.append(p['nome'])
        people_older_str += p['nome'] + ', '

print(f'Foram cadastradas um total de {len(people)} pessoas.')
print(f'A média de idade é {age_average:.1f} .')
print(f'Total de mulheres é {len(women_list)}, e elas são: {women_str[:-2]}.')  # [:-2] para tirar a vírugula e o espaço do último nome
print(f'{people_older_str[:-2]} possuem idade maior que a média, totalizando {len(people_older)} pessoas.')