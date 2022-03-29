# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def vote(year):
    import datetime
    age = datetime.date.today().year - year
    if age < 16:
        return f'Voto não autorizado para a idade de {age} anos.'
    elif 16 <= age < 18 or age > 65:
        return f'Voto facultativo para a idade de {age} anos.'
    else:
        return f'Voto obrigatório para a idade de {age} anos.'
y = int(input('Ano de nascimento: '))
print(vote(y))
