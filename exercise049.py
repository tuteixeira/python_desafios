# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

name = input('Qual seu nome? ')
num = float(input(f'Oi {name}, escolha um número: '))
print(f'O nº {num} é o meu nº da sorte, eu sei a tabuada completa dele:')
for c in range(1, 11):
    print(f'{num:2} x {c:2} = {num * c:2}')
