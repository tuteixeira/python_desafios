#faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Diga um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.' .format(ano))
else:
    print('Esse ano não é bissexto')