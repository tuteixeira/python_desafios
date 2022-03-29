#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, um diferente, ESCALENO: todos os lados diferentes.

print('Para saber que tipo de triângulo será formado, diga todos os segmentos: ')
seg1 = float(input('Segmento 1: '))
seg2 = float(input('Segmento 2: '))
seg3 = float(input('Segmento 3: '))
if seg1 + seg2 >= seg3 and seg2 + seg3 >= seg1 and seg1 + seg3 >= seg2:
    if seg1 == seg2 == seg3:
        print('O triângulo formado é: EQUILÁTERO')
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        # seg1 != seg2 !=seg3 != seg1
        print('O triângulo formado é: ISÓSCELES')
    else:
        print('O triângulo é: ESCALENO')
else:
    print('Os segmentos não formam um triângulo, tende novamente.')
