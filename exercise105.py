# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:- Quantidade de notas – A maior nota– A menor nota
# – A média da turma – A situação (opcional)

def notas(*n, sit=False):
    """
    - Recebe várias notas
    :param n: uma ou mais notas
    :return:  dict com : quantidade de notas; maior nota; menor nota; média de notas; situação OPCIONAL
    """
    r = dict()
    r.update({'Maior Nota': max(n), 'Menor Nota': min(n), 'Total de Notas': len(n), 'Média': sum(n)/len(n)})
    if sit:
        if r['Média'] < 6:
            r['Situação'] = 'Reprovado'
        else:
            r['Situação'] = 'Aprovado'
    return r
studant_note = notas(6, 6, 6, sit=True)
print(studant_note)
