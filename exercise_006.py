#Crie um algoritimo que leia um nº e mostre seu dobro, triplo e raiz quadrada

name = input('Qual teu nome? ')
print(f'Hello word e hello {name}, bom dia!')
n1 = int(input('Agora me diga um número: '))
dobro = n1 * 2
triplo = n1 * 3
rq = n1 ** (1/2)
print(f'{name} o dobro de {n1} vale {dobro}, já o triplo é {triplo} e a raiz quadrada é {rq:.2f}')


