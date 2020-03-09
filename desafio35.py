# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.


a = float(input('Digite o 1º segmento: '))
b = float(input('Digite o 2º segmento: '))
c = float(input('Digite o 3º segmento: '))
if a + b >= c and b + c >= a and c + a >= b:
#if abs(a-b) < c < a + b:
    print("É possível formar um triângulo, parabéns lixo.")
else:
    print("Não é possível transcrever um triângulo com esses valores, tosco vc.")
