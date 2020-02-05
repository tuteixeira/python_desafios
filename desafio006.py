#Crie um algoritimo que leia um nº e mostre seu dobro, triplo e raiz quadrada
nome = input('Falai, qual teu nome? ')
print('Hello word e hello {}, prazer parça!' .format(nome))
n1 = int(input('Agora me diga um número: '))
dobro = n1 * 2
triplo = n1 * 3
rq = n1 ** (1/2)
print('{} o dobro de {} vale {}, já o triplo é {} e a raiz quadrada é {:.3f}' .format( nome, n1, dobro, triplo, rq) ,end=' ')
print('Se bola que aki sou eu ..|.. ')
