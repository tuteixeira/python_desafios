#Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

count = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    num = int(input('Digite um valor de 0 até 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o nª {count[num]}.')
        continuar = ' '
        while continuar not in 'NS':
            continuar = str(input('Quer continuar? ')).upper().strip()[0]
        if continuar == 'N':
            break
