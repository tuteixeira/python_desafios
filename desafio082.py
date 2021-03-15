# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas


userlist = list()
oddlist = list()
evenlist = list()
continuar = ''
while True:
    num = int(input('Digite um valor: '))
    userlist.append(num)
    if num % 2 == 0:
        evenlist.append(num)
    else:
        oddlist.append(num)
    continuar = str(input('Deseja continuar? [ S/N ] ')).strip().upper()[0]
    while continuar not in 'NS':
        continuar = str(input('Digite -S ou F - ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Você digitou {len(userlist)} valores, sua lista é: {userlist}. Valores pares foram: {evenlist} e valores ímpares foram: {oddlist}')
