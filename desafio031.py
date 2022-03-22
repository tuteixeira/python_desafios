#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
#de até 200Km e R$0,45 parta viagens mais longas.~

dist = float(input('Qual a distância da sua viagem? '))
#valor = dist * 0.50 if dist <= 200 else dist * 0.45
if dist <= 200:
    valor = dist * 0.5
else:
    valor = dist * 0.45
print(f'Sua viagem custará {valor:.2f} reais.')


