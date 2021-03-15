# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

studant = dict()
studant['nome'] = str(input('Nome do aluno: '))
studant['média'] = float(input(f'Média do aluno {studant["nome"]}: '))

if studant['média'] < 5:
    studant['situação'] = 'REPROVADO'
elif 5 <= studant['média'] < 7:
    studant['situação'] = 'EM RECUPERAÇÃO'
else:
    studant['situação'] = 'APROVADO'
print('~' * 25)
for k, v in studant.items():
    print(f'   ~ {k} é: {v}')


