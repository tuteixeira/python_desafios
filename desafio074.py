#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
list = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100),)
print(f'A lista gerada foi: {list}')
print(f'Dessa lista, o nº {(max(list))} é o maior e o {(min(list))} é o menor.')





