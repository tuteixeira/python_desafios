# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas

user_list = list()
odd_list = list()
even_list = list()
keep = ''
while True:
    num = int(input('Digite um valor: '))
    user_list.append(num)
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
    keep = str(input('Deseja continuar? [ S/N ] ')).strip().upper()[0]
    while keep not in 'NS':
        keep = str(input('Digite -S ou F - ')).strip().upper()[0]
    if keep == 'N':
        break
print(f'Você digitou {len(user_list)} valores, sua lista é: {user_list}. Valores pares foram: {even_list} e valores ímpares foram: {odd_list}')
