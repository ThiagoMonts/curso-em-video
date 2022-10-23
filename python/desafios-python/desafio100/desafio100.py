from random import randint

numeros = []
par = []
def sorteia():
    print('Sorteando os 5 valores da lista: ', end='')
    for num in range(0,5):
        n = randint(1, 10)
        numeros.append(n)
        print(n, end=' ')
    print('PRONTO!')

def somaPar():
    s = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            par.append(v)
            s += v
    print(f'Somando os valores pares de {numeros}, temos {s}')


sorteia()
somaPar()