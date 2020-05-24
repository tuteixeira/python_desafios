#Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.


print('A soma de todos os nº múltiplos de 3 de 1 até 500 é: ')
soma = 0
contador = 0
for c in range(1, 501, +2):
    if c % 3 == 0:
        contador += + 1# tb pode ser escrito como: contador = contador + 1
        soma += c# tb pode ser escrito como: soma = soma + c
print('A soma dos {} valores é {}.' .format(contador, soma))













