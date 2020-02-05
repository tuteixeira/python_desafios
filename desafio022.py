#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas.Quantas letras ao todo (sem considerar espaços).Quantas letras tem o primeiro nome.
nome = str(input('Qual seu nome completo? ')).strip()
pn = nome.split()
print('Oi {}, vou analisar seu nome: ' .format(pn[0]))
print('Seu nome em maiúculas é: {}' .format(nome.upper()))
print('Seu nome em minúsculas é: {}' .format(nome.lower()))
print('Seu nome completo possuo {} letras.' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome {} possui {} letras.' .format(pn[0], len(pn[0])))