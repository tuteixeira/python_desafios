#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta 2.0m²
def multiply(x, y):
    return x * y


def dividir(x, y):
    return x / y

nome = input('Oi, qual nome da sua empresa: ')
print('Ok {}, bem vindo. \nSe você está aqui é porque precisa calcular quanto de tinta irá usar para pintar sua parede. Para isso basta me dizer a largura e altura da sua parede.' .format(nome))
print('OBS: DIGA EM METROS E USE . AO INVÉ DE , ')
largura = float(input('Largura: '))
altura = float(input('Altura: '))
qt = dividir(multiply(largura, altura), 2)
area = multiply(largura, altura)
print('Hum ... então a área da sua parede vale {:.3f} m², e vc usará {:.3f} L de tinta' .format(area ,qt))





