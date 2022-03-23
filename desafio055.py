#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

bigger = 0
smaller = 0
for w in range (1,6):
    weight = float(input(f'Digite o peso da {w}º pessoa: '))
    if w == 1:
        bigger = weight
        smaller = weight
    else:
        if weight > bigger:
            bigger = weight
        if weight < smaller:
            smaller = weight
print(f'O maior peso é {bigger} e o menor peso é {smaller}.')

# heavy = 0
# light = 0
# ph = 0
# pl = 0
# for p in range(1,6):
#     weight = float(input(f'Digite o peso da {p}º pessoa: '))
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
# print(f'O maior peso é da {ph}ª pessoa [{heavy}] e a {pl}ª pessoa tem o menor peso [{light}].')