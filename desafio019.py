#Exercício Python 019: Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
print('Bom dia profª, escreva o nome dos alunos:')
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
sorteio = random.choice([a1, a2, a3, a4])
print(f'O aluno {sorteio} irá apagar o quadro.')

