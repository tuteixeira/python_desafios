# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto, à vista no cartão: 5% de desconto, em até 2x no cartão: preço formal, 3x ou mais no cartão: 20% de juros.

print('\033[1;31;40m❤❤❤ Loja Teixeira ❤❤❤\033[m')
value = float(input('Valor da compra: R$ '))
payment = int(input("""Digite\033[1;31m 1\033[m : Para pagamento à vista no dinheiro;
Digite\033[1;31m 2\033[m : Para pagamento à vista com cartão;
Digite\033[1;31m 3\033[m : Para pagamento em até 2 vezes no cartão;
Digite\033[1;31m 4\033[m : Para pagamento até 3 vezes ou mais no cartão;
\033[4mQual forma de pagamento?\033[m """))
in_cash = value - (value * 0.10)
in_card = value - (value * 0.05)
more2times_card = value + (value * 0.20)
if payment == 1:
    print(f'Sua compra de R${value:.2f} com 10% de desconto passará a custar R${in_cash:.2f}.')
elif payment == 2:
    print(f'Sua compra de R${value:.2f} com 5% de desconto passará a custar R${in_card:.2f}.')
elif payment == 3:
    print('A forma de pagamento escolhida não lhe confere desconto algum.')
elif payment == 4:
    print(f'Sua compra de R${value:.2f} passará a custar R${more2times_card:.2f} com 20% a mais de juros.')
else:
    print('Forma de pagamento indisponível, tente novamente.')
