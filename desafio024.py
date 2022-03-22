#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input(' Qual cidade você mora? ')).strip()
print('Sua cidade começa com a palavra Santo?')
print(cidade[:5].upper() == 'SANTO')
