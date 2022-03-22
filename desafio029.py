#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual sua atual velocidade? '))
if v > 80:
    print('Voce foi multado por excesso de velocidade!')
    m = (v-80) * 7
    print(f'Você pagará R${m:.2f} de multa, melhore!')
else:
    print('Dirija em segurança!')
