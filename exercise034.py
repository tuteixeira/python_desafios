#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite seu salário para eu calcular seu aumento: R$ '))
if sal <= 1250:
    new_sal = sal + (sal * 15 / 100)
else:
    new_sal = sal + (sal * 10 / 100)
print(f'Seu salário passou de R$ {sal:.2f} para R$ {new_sal :.2f}.')
