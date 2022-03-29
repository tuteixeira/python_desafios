# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('Digite o Primeiro número da P.A: '))
razao = int(input('Digite a Razão da P.A: '))
for c in range(1, 11):
    print(num, end= ' -> ')
    num += razao
print('Fim da contagem')

# firstelement = int(input('Qual o 1º termo de sua P.A? '))
# commomdifference = int(input('Qual é a razão da sua P.A? '))
# tenth = firstelement + (11 - 1) * commomdifference
# for c in range(firstelement, tenth , + commomdifference):
#     print(c)
