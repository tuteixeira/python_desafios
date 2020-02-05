# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
cliente = input('Qual seu nome? ')
km = float(input('Olá {}, qnts KM vc percorreu? ' .format(cliente)))
dia = int(input('Diga em dias quanto durou sua viagem: '))
#diariaD = 60 * dia
#diariaK = km * 0.15
#total = diariaD + diariaK
total = (60 * dia) + (km * 0.15)
print('Sabendo que a diária vale R$ 60,oo e o KM roado custa R$ 0,15 ; vc pagará {:.2f} R$.' .format(total))