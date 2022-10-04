valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'A quantidade de números digitados foi {len(valores)}.')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente é {valores}.')
if 5 in valores:
    print('Sim, o número 5 faz parte da lista.')
else:
    print('Não, o número 5 não faz parte da lista.')