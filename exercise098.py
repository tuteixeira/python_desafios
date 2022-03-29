# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1 . b) de 10 até 0, de 2 em 2 , c) uma contagem personalizada

def contador(initial, final, pace):
    print(f'~' * 30)
    print(f'Contando de {initial} até {final} pulando de {pace} em {pace}.')
    if initial < final and pace < 0:
        print(f'Não é possível essa interação, ela precisa ser negativa.')
        return
    elif initial > final and pace > 0:
        print(f'Não é possível essa interação, ela precisa ser postiva ')
        return
    elif initial == final:
        print(f'Não é possível usar essa interação se o início {initial} e o fim {final} são iguais.')
        return
    elif pace == 0:
        print(f'Não é possível usar 0 como interação.')
        return
    if pace > 0:
        final += 1
    else:
        final -= 1

    for cont in range(initial, final, pace):
        print(cont, end=' ')
    print(f'FIM')

contador(1, 10, 1)
contador(10, 1, -2)
print(f'~' * 30)
while True:
    i = int(input('Digite o início da contagem: '))
    f = int(input('Digite o final da contagem: '))
    p = int(input('Digite a interação: '))
    contador(i, f, p)
    sair = str(input('Deseja sair? [ S/N ] ')).upper().strip()
    while sair not in 'SN':
        sair = str(input('Para sair digite [ S/N ] ')).upper().strip()
    if sair == 'S':
        break
