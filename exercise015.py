#Exercício Python 015: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

cliente = input('Qual seu nome? ')
km = float(input(f'Olá {cliente}, qnts KM vc percorreu? '))
dia = int(input('Diga em dias quanto durou sua viagem: '))
#diariaD = 60 * dia
#diariaK = km * 0.15
#total = diariaD + diariaK
total = (60 * dia) + (km * 0.15)
print(f'Sabendo que a diária vale R$ 60,oo e o km rodado custa R$ 0,15 ; vc pagará {total:.2f} R$.')
