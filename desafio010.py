#Exercício Python 010: Crie um programa que leia qnt de dinheiro uma pessoa tem na carteira e qnt de dollar ela pode comprar (Dollar = RS 3,27)

nome = input('Nome: ')
real = float(input(f'Ok {nome}, qual valor você tem na carteira ? obs: ESCREVA USANDO . AO INVÉS DE , \nR$ ' ))
dollar = (real / 3.27)
print(f'Ao converter esse valor para Dollar você terá: {dollar:.2f}')


