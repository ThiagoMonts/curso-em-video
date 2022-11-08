def notas (*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict() #Nesse caso o r será um dicionário
    r['total'] = len(n) #O total será o total de notas que foi passado, por isso é usado o len(n)
    r['maior'] = max(n) #Será guardado o valor máximo de n
    r['menor'] = min(n) #Será guardado o valor mínimo de n
    r['média'] = sum(n) / len(n) #A média será a soma de n (sum) divido pela quantidade de elementos (len(n))
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa principal
resp = notas(5.5, 2.5, 1.5, sit = True)
print(resp)
#help(notas)
