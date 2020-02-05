#Crie um programa que leia qnt de dinheiro uma pessoa tem na carteira e qnt de dollar ela pode comprar (Dollar = RS 3,27)
nome = input('Oi, qual seu nome? ')
real = float(input('Ok {}, qnt vc tem na carteira ? obs: ESCREVA USANDO . AO INVÉS DE ,   R$' .format(nome)))
dollar = (real / 3.27)
print('Eita, pouco ... mas pouco mesmo é se a gente converter pra Dollar, pq vai dar {:.2f}' .format(dollar))


