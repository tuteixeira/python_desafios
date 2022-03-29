# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    # tam = len(num)
    # print(f'Existem {tam} elementos e o maior é {max(num)}.')
    maior = cont = 0
    for i, v in enumerate(num):
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'O maior valor é {maior}')
maior(0, 1, 2)
maior(0)
maior(100, 90, 80, 70)
maior(10, 10)
maior()
