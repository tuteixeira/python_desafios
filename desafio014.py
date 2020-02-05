#Conversão de uma temperatura de ºC para ºF e K
C = float(input('Qual temperatura do líquido em º Celcius? '))
F = 1.8 * C + 32
K = C + 273
print('A temperatura do líquido de {} ºC é de {} ºF e {} K.' .format(C, F, K))
