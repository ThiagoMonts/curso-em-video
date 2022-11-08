lista = list()
Pares = list()
Impares = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        Pares.append(n)
    else:
        Impares.append(n)
    r = str(input('Deseja continuar [S/N]? '))
    if r in 'Nn':
        break
print(f'A lista completa digitada foi {lista}.')
print(f'A lista só com números pares é {Pares}.')
print(f'A lista só com números ímpares é {Impares}.')