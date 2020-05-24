# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto, à vista no cartão: 5% de desconto, em até 2x no cartão: preço formal, 3x ou mais no cartão: 20% de juros.

print('\033[1;31;40m❤❤❤ Loja da Tuki ❤❤❤\033[m')
valor = float(input('Valor da compra: R$ '))
pagamento = int(input("""Digite\033[1;31m 1\033[m : Para pagamento à vista no dinheiro;
Digite\033[1;31m 2\033[m : Para pagamento à vista com cartão;
Digite\033[1;31m 3\033[m : Para pagamento em até 2 vezes no cartão;
Digite\033[1;31m 4\033[m : Para pagamento àem 3 vezes ou mais no cartão;
\033[4mQual forma de pagamento?\033[m """))
avistanodinheiro = valor - (valor * 0.10)
avistanocartao = valor - (valor * 0.05)
tresxoumaisnocartao = valor + (valor * 0.20)
if pagamento == 1:
    print('Sua compra de R${:.2f} com 10% de desconto passará a custar R${:.2f}.'.format(valor, avistanodinheiro))
elif pagamento == 2:
    print('Sua compra de R${:.2f} com 5% de desconto passará a custar R${:.2f}.'.format(valor, avistanocartao))
elif pagamento == 3:
    print('A forma de pagamento escolhida não lhe confere desconto algum.')
elif pagamento == 4:
    print('Sua compra de R${:.2f} passará a custar R${:.2f} com 20% a mais de juros.'.format(valor, tresxoumaisnocartao))
else:
    print('Forma de pagamento indisponível, tente novamente.')


