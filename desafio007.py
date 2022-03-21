#Desenvolva um programa que leia duas notas de um aluno e calcule a sua média

aluno = str(input('Nome do aluno: '))
nota1 = int(input('Então me diga sua nota em Bio: '))
nota2 = int(input(f'Agora {aluno} me diga a nota de Geo: '))
media = ((nota1 + nota2) / 2)
print(f'A média vale: {media}')



