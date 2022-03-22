#Exercício Python 013: Faça um algorítmo que leia o salário de um funcionário e mostreseu novo salário com 15% de aumento.

s_atual = float(input('Salário atual: R$ '))
s_novo = s_atual + (s_atual * 15 / 100)
print(f'Com o reajuste de 15% a mais, o salário passará de {s_atual} R$ para {s_novo:.2f} R$.')