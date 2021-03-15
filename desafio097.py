# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def escreva(text):
    print(f'~' * (len(text) + 4))
    print(f'  {text}')
    print(f'~' * (len(text) + 4))


phrase = str(input('Digite uma frase: '))
escreva(phrase)


