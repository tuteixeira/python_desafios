#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

list = []
while True:
    l = int(input('Digite um valor: '))
    if l not in list:
        list.append(l)
        print('Valor adicionado')
    else:
        print('Valor duplicado não é adicionado')
    answer = str(input('Deseja continuar a adiconar nº? [S/N]  ')) .strip() .upper()[0]
    while answer not in 'NS':
        answer = str(input('Digite [S/N]: ')) .strip() .upper()[0]
    if answer in 'N':
        break
list.sort()
print(f'Sua lista é {list}')
