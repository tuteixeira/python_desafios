#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

nome = input('Oi, qual seu nome? ')
print(f'Ok {nome}, você efeutou uma compra em nossa loja, essa compra foi no valor de:', end='')
valor = float(input(' R$ '))
desc = valor - (valor * 5 / 100)
print(f'Nossas lojas estão com desconto de 5%, ou seja, agora vc pagará apenas: R$ {desc :.2f}.')


