#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

list = ('Tuira', 'Alice', 'Flavio', 'Clarissa', 'Marcia', 'Tais', 'Raimundo', 'Nina', 'Caya', 'Lana')
for words in list:
    print(f'\nA palavra {words.upper()} possui as vogais : ', end=' ')
    for vog in words:
        if vog.upper() in 'AEIOU':
            print(vog, end=' ')