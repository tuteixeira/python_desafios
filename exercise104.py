# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função
# input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(text):
    ok = False
    valor = 0
    while True:
        nr = str(input(text)).strip()
        if nr.isnumeric():
            valor = int(nr)
            ok = True
        else:
            print('Erro! Digite um número inteiro válido')

        if ok:
            break
    return valor
n = leiaInt('Digite um nº: ')
print(f'Vc digitou {n}')
