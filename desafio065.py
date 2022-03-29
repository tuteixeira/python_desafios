#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


quantidade = soma = media = maior = menor = 0
resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um nº: '))
    resposta = str(input('Quer continuar? [S/N] ')) .upper() .strip()
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        elif num > maior:
            maior = num
media = soma / quantidade
print(f'Você digitiu {quantidade} números. A média é de {media:.2f}, o maior valor é {maior} e o menor é {menor}.')
