#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO, Média entre 5.0 e 6.9: RECUPERAÇÃO, Média 7.0 ou superior: APROVADO

print('\033[2;30;41mATENÇÃO\033[m\nPara verificar sua situação, preencha os campos abaixo: ')
nome = str(input('Nome: '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Seguda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Parabéns {}, sua média é de {:.2f} e você foi apovado!' .format(nome, media))
elif media < 5:
    print('Sinto muito {}, sua média é de {:.2f}, você está reprovado!' .format(nome, media))
else:
    print('{}, você está de recuperação pois sua média é de {:.2f}.' .format(nome, media))

