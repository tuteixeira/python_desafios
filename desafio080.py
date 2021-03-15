#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

print('Olá, digite 5 números que eu te digo as suas posições correspondentes.')
userlist = list()
for cont in range(0,5):
    num = int(input('Digite um valor: '))
    if cont == 0:
        userlist.append(num)
        print('Valor add no início da Lista.')
    elif num > userlist[-1]:
        userlist.append(num)
        print('Valor add no final da lista.')
    else:
        position = 0
        while position < len(userlist):
            if num <= userlist[position]:
                userlist.insert(position, num)
                print(f'Valor add na posição {position} na lista.')
                break
            position += 1
print(f'Os valores da sua lista em ordem são: {userlist}')
