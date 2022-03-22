#Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('A soma de todos os nº múltiplos de 3 entre 1 até 500 é: ')
sum = 0
counter = 0
for c in range(1, 501, +2):
    if c % 3 == 0:
        counter += + 1 #tb pode ser escrito como: contador = contador + 1
        sum += c #tb pode ser escrito como: soma = soma + c
print(f'Os {counter} valores somados valem {sum}.')













