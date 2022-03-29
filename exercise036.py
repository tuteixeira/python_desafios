#Exercício Python 036: Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('Bem vindo ao site \033[1;34mQUERO CASA\033[m')
nome = str(input('Digite seu nome para simularmos seu empréstimo e as condições bancárias: '))
valor = float(input('O valor da casa a qual pretende comprar é de: R$ '))
salario = float(input(f'{nome} seu salário atual é: R$ '))
tempo = int(input('Em quantos anos pretende pagar? '))
parcela = valor / (tempo * 12)
if parcela >= salario * 30 / 100:
    print(f'{nome} a parcela de {parcela:.2f} é superior a 30% do salário\n\033[1;31mO EMPRÉSTMO FOI NEGADO.\033[m')
else:
    print(f'{nome} a parcela de {parcela:.2f} é acima do permitido para o seu salário\n\033[1;31mSEU EMPRÉSTIMO FOI ACEITO\033[m')
