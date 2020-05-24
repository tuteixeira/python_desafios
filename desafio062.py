# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.


num = int(input('Digite um nº: '))
r = int(input('Digite a razão da P.A: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print(num, end=' -> ')
        num += r
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
print('FIM')
print('Vc usou {} termos.' .format(total))