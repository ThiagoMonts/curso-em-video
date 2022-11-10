'''cont = 1
while cont <= 10:
    print(cont,' -> ', end=' ')
    cont += 1
print('Acabou')'''

'''cont = 1
while True: #Loop infinito
    print(cont,' -> ', end=' ')
    cont += 1
print('Acabou')'''1

n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')