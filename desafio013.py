#Faça um algorítmo que leia o salário de um funcionário e mostreseu novo salário com 15% de aumento.
salatual = float(input('Salário atual: R$ '))
salnovo = salatual + (salatual * 15 / 100)
print('Com o reajuste de 15% a mais, o salário passará de {} R$ para {:.2f} R$.' .format(salatual, salnovo))