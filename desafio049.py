# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

name = input('Qual seu nome? ')
num = float(input('Oi {}, escolha um número : ' .format(name)))
print('Boa escolha, o nº {} é o meu nº da sorte, eu sei a tabuada completa dele, se liga:' .format(num))
for c in range(1, 11):
    print('{:2} x {:2} = {:2}' .format(num, c, num * c))
