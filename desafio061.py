# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

num = int(input('Digite um nº: '))
r = int(input('Digite a razão da P.A: '))
c = 0
while c < 10:
    print(num, end=' -> ')
    num += r
    c += 1
print('Fim da contagem')
