# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um nº inteiro: '))
base = int(input("""Escolha a base numérica que você quer converter:
Digite\033[1;33m 0\033[m para \033[1;33mBinário\033[m
Digite\033[1;33m 1\033[m para \033[1;33mOctal\033[m
Digite\033[1;33m 2\033[m para \033[1;33mHexadecimal\033[m
Qual nº vc escolhe? """))
if base == 0:
    print(f'O nº {num} convertido para BINÁRIOI é: {bin(num)[2:]}.')
elif base == 1:
    print(f'O nº {num} convertido em OCTAL é: {oct(num)[2:]}.')
elif base == 2:
    print(f'O nº {num} convertido para HEXADECIMAL é: {hex(num)[2:]}.')
else:
    print('Opção inválida')




