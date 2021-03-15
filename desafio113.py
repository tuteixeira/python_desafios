# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[31mError \033[m')
            continue
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[31mError\033[m')
            continue
        else:
            return n



num_int = leia_int('Digite um valor inteiro: ')
num_float = leia_float('Digite um valor flutuante: ')
print(f'Você digitou o valor inteiro {num_int} e o valor {num_float} flutuante.')
