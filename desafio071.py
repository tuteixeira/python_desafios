#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Valor do saque: R$ '))
total = valor
n20 = n10 = n1 = 0
ced = 50
while True:
    n = total // ced
    total -= n * ced
    print(f'Vc usou {n} notas de {ced}')
    if total == 0:
        break
    else:
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1





