#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).Quantas letras tem o primeiro nome.

name = str(input('Qual seu nome completo? ')).strip()
first_name = name.split()
name_count_space = name.count(' ')
print(f'Oi {first_name[0]}, vou analisar seu nome: ')
print(f'Seu nome em maiúculas é: {name.upper()}')
print(f'Seu nome em minúsculas é: {name.lower()}')
print(f'Seu nome completo possui {len(name) - name_count_space} letras.')
print(f'Seu primeiro nome {first_name[0]} possui {len(first_name[0])} letras.')