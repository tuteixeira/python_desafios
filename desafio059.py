#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.


num1 = int(input('Digite um nº: '))
num2 = int(input('Digite outro nº: '))
option = 0
while option != 5:
    print("""
Digite \033[34m[1]\033[m para somar
Digite \033[34m[2]\033[m para multiplicar
Digite \033[34m[3]\033[m para ver qual é o maior valor
Digite \033[34m[4]\033[m para digitar novos númeors
Digite \033[34m[5]\033[m para sair do programa 
""")
    option = int(input('\033[34m >>> \033[m Escolha qual opção vc deseja: '))
    if option == 1:
        sum = num1 + num2
        print('A soma entre {} e {} é \033[34m{}\033[m.' .format(num1, num2, sum))
    elif option == 2:
        multiplication = num1 * num2
        print('A multiplicação de {} com {} é \033[34m{}\033[m.' .format(num1, num2, multiplication))
    elif option == 3:
        if num1 > num2:
            print('\033[34m{}\033[m é maior que \033[34m{}\033[m.' .format(num1, num2))
        else:
            print('\033[34m{}\033[m é maior que \033[34m{}\033[m.' .format(num2, num1))
    elif option == 4:
        num1 = int(input('Digite um nº: '))
        num2 = int(input('Digite outro nº: '))
    elif option == 5:
        print('FIM, volte sempre')
    else:
        print('Opção inválida')




