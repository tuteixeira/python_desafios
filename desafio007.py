#Desenvolva um programa que leia duas notas de um aluno e calcule a sua média
aluno = str(input(' Oi, qual seu nome aluno ignorante? '))
print('Hum ... se vc está aki é pq quer saber as médias das suas notas, certo?')
nota1 = int(input('Então me diga sua nota em Bio: '))
nota2 = int(input('Agora {} me diga a nota de Geo: ' .format(aluno)))
media = ((nota1 + nota2) / 2)
print('Deu {}' .format(media))



