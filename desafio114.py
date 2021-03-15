# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.


import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Error')
else:
    print('Possível acessar o site http://pudim.com.br/')