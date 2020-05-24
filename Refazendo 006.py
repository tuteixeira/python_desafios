from math import sqrt
from time import sleep

nome = '\033[1m' + input('Fala viadX, qual seu nome? ') + '\033[m'
if nome == '\033[1m\033[m':
    print('Vc n colocou seu nome, enfim')
    exit(1)
print('Prazer {}, bora jogar pq eu tô entediada na quarentena.' .format(nome))
num = float(input('Eu vou descobrir o dobro, o triplo e a raíz quadrada do nº q vc digitar \nDigita ai {}: ' .format(nome)))
dobro = num * 2
triplo = num * 3
raiz = sqrt(num)
print('Porra, mas tu escolheu um nº difícil, podia ser quaqluer um, mas \033[31m{}\033[m é brabo\nPeraí q tenho q calcular\n . . . ' .format(num))
sleep(4)
print('Pera q tô com \033[4mdificuldade real\033[m')
sleep(3)
print('Entao {}, o triplo é {}, o dobro vale {} e a raíz {:.2f}.' .format(nome, dobro, triplo, raiz))
sleep(3)
print('\033[1;33mMamacia é sinistra\033[m')