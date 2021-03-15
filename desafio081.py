#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
# A) Quantos números foram digitados.B) A lista de valores, ordenada de forma decrescente.C) Se o valor 5 foi digitado e está ou não na lista.

print('Olá, vou analisar os nº que você digitar')

list = []

while True:
    list.append(int(input('Digite um nº: ')))
    answer = ' '
    while answer not in 'NS':
        answer = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if answer in 'N':
        break
list.sort(reverse=True)

print(f'Sua lista possui {len(list)} termos.')
print(f'A ordem decrescente é: {list}')
if 5 in list:
    print(f'O nº 5 foi digitado ')
else:
    print('O valor nº 5 não foi digitado.')


# userlist = list()
# continuar = ' '
# cont = number5 = 0
# while True:
#     num = int(input('Digita um valor: '))
#     userlist.append(num)
#     cont += 1
#     if 5 == num:
#         number5 += 1
#     continuar = str(input('Quer continuar? [ S/N ] ')).strip().upper()[0]
#     while continuar not in 'NS':
#         continuar = str(input('Digite - S ou N - ')).strip().upper()[0]
#     if continuar == 'N':
#             break
# userlist.sort(reverse=True)
#
# print(f'Você digitou {cont} valor/valores e a sua lista em ordem decrescente é {userlist}. O valor número 5 foi digitado {number5} vez/vezes.')