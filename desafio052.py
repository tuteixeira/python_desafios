#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


#n = int(input('digite um número: '))
#if n==2 or n==3 or n%2 !=0 and n%3 !=0:
#    print('Esse é um número primo!')
#else:
#    print('Esse NÃO é um número primo!')




num = int(input('Digite um nº: '))
if num != 2 and num % 2 == 0:
    print('n primo')
elif num % 3 == 0 and num != 3:
    print('n primo')
elif num % 5 == 0 and num != 5:
    print('n primo')
elif num % 7 == 0 and num != 7:
    print('n primo')
elif num == 1:
    print('n primo')
else:
    print('primo')