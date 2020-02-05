#Escreva um programa que leia um valor em metros e o exiba convertido em cm e ml
nome = input('Oi, qual seu nome? ')
print('Prazer em te conhecer {}' .format(nome) ,end='')
altura = float(input(', qual sua altura em metros? '))
cm = (altura * 100)
ml = (altura * 1000)
print('Sua altura {}m passada para cm vale {:.2f}cm e em mm vale {:.2f}mm' .format(altura, cm, ml))
