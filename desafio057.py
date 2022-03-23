#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sex = str(input('Digite seu sexo: [F/M] ')).strip().upper()
while sex not in 'MF':
    sex = str(input('Dados inválidos, digite novamente seu sexo: [F/M] ')).strip().upper()
print(f'Sexo {sex} cadastrado com sucesso.')