#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm

nome = input('Oi, qual seu nome? ')
print(f'ok, vamos começar {nome}' ,end='')
altura = float(input(', qual sua altura em metros? '))
cm = (altura * 100)
ml = (altura * 1000)
print(f'Sua altura {altura}m passada para cm vale {cm:.2f}cm e em mm vale {ml:.2f}mm')
