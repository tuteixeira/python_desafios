n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Invalido Tente novamente ', end='')
    else:
        print(f'Você digitou o número {n[num]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:=^30}'.format(' PROGRAMA FINALIZADO '))