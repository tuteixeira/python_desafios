#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta 2.0m²

nome = input('Nome da empresa: ')
print(f'Ok {nome}, bem vindos. \nSe você está aqui é porque precisa calcular quanto de tinta irá usar para pintar sua parede.Para isso basta me dizer a largura e altura da sua parede.')
print('OBS: DIGA EM METROS E USE . AO INVÉ DE , ')
largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
qt = area / 2
print(f'Hum ... então a área da sua parede vale {area:.3f} m², e vc usará {qt:.3f} L de tinta')





