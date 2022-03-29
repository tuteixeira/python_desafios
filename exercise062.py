# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

num = int(input('Digite um nº: '))
r = int(input('Digite a razão da P.A: '))
c = 0
total = 0
more = 10
while more != 0:
    total += more
    while c < total:
        print(num, end=' -> ')
        num += r
        c += 1
    print('Pausa')
    more = int(input('Quantos termos vc quer mostrar a mais? '))
print('FIM')
print(f'Você analisou {total} termos.')
