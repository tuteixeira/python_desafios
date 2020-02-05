#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input(' Digite uma frase qualquer: ')) .strip() .upper()
print('A letra A apareceu {} vezes.' .format(frase.count('A')))
print('A letra A aparece 1ª vez na posição {} .' .format(frase.find('A')+1))
print('O A aparece pela última vez na posição {} .' .format(frase.rfind('A')+1))
