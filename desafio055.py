#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for p in range (1,6):
    peso = float(input('Digite o peso do {}º membro: ' .format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            pmenor = peso
print('O maior peso é {} e o menor peso é {}.' .format(maior, menor))



# heavy = 0
# light = 0
# ph = 0
# pl = 0
# for p in range(1,6):
#     weight = float(input('Digite o peso da {}º pessoa: ' .format(p)))
#     if p == 1:
#         heavy = weight
#         light = weight
#         ph = pl = p
#     else:
#         if weight > heavy:
#             heavy = weight
#             ph = p
#         if weight < light:
#             light = weight
#             pl = p
# print('O maior peso é  da {}ª pessoa [{}] e a {}ª pessoa tem o menor peso [{}].' .format(ph, heavy, pl, light))