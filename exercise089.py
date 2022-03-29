# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

final_list = list()
while True:
    name = str(input('Nome do aluno: '))
    note1 = float(input('Nota 1: '))
    note2 = float(input('Nota 2: '))
    final_list.append([name, note1, note2])
    keep = str(input('Continar? [ S/N ] ')).strip().upper()[0]
    while keep not in 'SN':
        keep = str(input('Digite: -S ou N- ')).strip().upper()[0]
    if keep == 'N':
        break
print('~' * 50)
print('Número do aluno ~ Nome do aluno ~ Média do aluno')
for pos, studant in enumerate(final_list):
    mean = (studant[1] + studant[2]) / 2
    print(f'{pos:^15} ~ {studant[0]:^13} ~ {mean:^10} ')
print('~' * 50)
print('Para mais informações, digite o número do aluno\n'
      '\033[31m[ PARA SAIR DIGITE 999 ]\033[m')
while True:
    num_studant = int(input('Número do aluno: '))
    if num_studant == 999:
        print('Fim')
        break
    if num_studant > len(final_list):
        print('Número inválido')
    else:
        print(f'O aluno {final_list[num_studant][0]}, tirou na 1º nota: {final_list[num_studant][1]} e tirou na 2º: {final_list[num_studant][2]}')
