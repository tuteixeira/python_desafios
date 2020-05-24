# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso, Entre 18,5 e 25: Peso Ideal, 25 até 30: Sobrepeso, 30 até 40: Obesidade, Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** altura
if imc <= 18.5:
    print('Seu IMC é {:.2f}, você está COM BAIXO DO PESO.' .format(imc))
elif imc <= 25:
    print('Seu IMC é {:.2f}, você está NO PESO IDEAL.' .format(imc))
elif imc <= 30:
    print('Seu IMC é {:.2f}, você está COM SOBREPESO.' .format(imc))
elif imc <= 40:
    print('Seu iMC é {:.2f}, você está COM OBESIDADE.' .format(imc))
else:
    print('SEu IMC é {:.2f}, você está com OBESIDADE MÓRBIDA.' .format(imc))