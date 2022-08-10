from random import randint
from time import sleep
print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*30)
num = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
n = randint(0,5)
if num == n:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print(f'GANHEI! Eu pensei no número {n} e não no {num}.')