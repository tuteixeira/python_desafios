#Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Os números pares que estão no intervalo entre 1 e 50 são: ')
for c in range(2, 51, +2):
    print(f'\033[4m {c}', end='')

#  A forma anterior é a forma mais eficiente, porém a form "correta" é:
#print('Os números pares que estão no intervalo entre 1 e 50 são: ')
#for c in range(1, 51):
#    if c % 2 == 0:
#        print(f'\033[4m {c}', end='')
