'''
#Forma com importação
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(num)
print(f'O fatorial de {n} é {f}')'''

#Forma com While
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

'''
#Forma com for
n = int(input('Digite um número para calcular o fatorial: '))
f = 1
for c in range (n,1, -1):
    f *= c
    c -= 1
print(f'O fatorial de {n} é {f}')'''