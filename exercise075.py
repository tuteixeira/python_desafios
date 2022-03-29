# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

pair = 0
num = (int(input('Digite um nº: ')), int(input('Digite outro nº: ')), int(input('Digite outro nº: ')),
       int(input('Digite o último nº: ')))
print(f'Analisando a lista: {num}')
print(f'O valor 9 apareceu {num.count(9)} vez/vezes;')
if 3 in num:
    print(f'O 1º valor 3 foi digitado na {num.index(3,0)+1} posição; ')
else:
    print('O 3 não foi digitado nenhuma vez;')
print('Os valores pares são: - ', end=' ')
for n in num:
    if n % 2 == 0:
        pair += 1
        print(n, end=' , ')
print(f'totalizando {pair} nº pares.')
