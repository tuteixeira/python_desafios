#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000.  C) qual é o nome do produto mais barato.

count = total = more1000 = low = 0
cheaper = ''
while True:
    product = str(input('Digite o produto: '))
    price = float(input(f'Digite o preço de \033[1;30m{product}\033[m: R$ '))
    total += price
    count += 1
    if count == 1 or price < low:
        low = price
        cheaper = product
    if price > 1000:
        more1000 += 1
    keep = ' '
    while keep not in 'SN':
        keep = str(input('Cadastrar mais produtos? \033[1m[S/N]\033[m ')).upper().strip()[0]
    if keep == 'N':
        break
print(f'''- Você cadastrou \033[1;30m{count}\033[m produto(s)
- O total foi R$ \033[1;30m{total:.2f}\033[m
- Existe \033[1;30m{more1000}\033[m artigos mais caros que R$ 1000.00 
- A compra mais barata é \033[1;30m{cheaper}\033[m custa R$ \033[1;30m{low}\033[m''')