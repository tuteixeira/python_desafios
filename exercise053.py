# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Qual a frase? ").upper().replace(" ", ""))
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")

# phrase = str(input('Digire uma frase: ')).upper() .strip() .split()
# join = ''.join(phrase)
# print(join, ' - ', join[::-1])
# if join == join[::-1]:
#     print('Trata-se de um políndromo')
# else:
#     print('Não trata-se de um políndromo')


# frase = str(input('Digite uma frase: ')) .upper() .strip()
# palavras = frase.split()
# junto = '' .join(palavras)
# inverso = junto[::-1]
# if inverso == junto:
#     print(f'A palavra {junto} é igual ao seu palíndromo {inverso}.')
# else:
#     print(f'A palavra {junto} não é igual a {inverso}, logo, isso não é um palindromo.')


# frase = str(input('Escreva uma frase: ')).strip() .upper()
# palavras = frase.split()
# junto = '' .join(palavras)
# inverso = ''
# for c in range(len(junto) -1, -1, -1):
#     inverso = inverso + junto[c]
# print(junto, inverso)
# if junto == inverso:
#     print('Palindro')
# else:
#     print('Não é um palindro')
