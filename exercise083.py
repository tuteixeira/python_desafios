# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

count = 0
expression = str(input('Digite sua expressão: '))
for x in expression:
    if x == '(':
        if count < 0:
            break
        count += 1
    elif x == ')':
        count -= 1
if count == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
