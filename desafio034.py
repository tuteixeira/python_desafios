#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite seu salário para eu calcular seu aumento: R$ '))
if sal <= 1250:
    nsal = sal + (sal * 15 / 100)
else:
    nsal = sal + (sal * 10 / 100)
print('Seu salário passou de R$ {:.2f} para R$ {:.2f}.' .format(sal, nsal))
