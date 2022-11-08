from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num: #Para cada valor in número
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0: #Se o contador for igual a zero, ou seja, não tenho número nenhum analisado
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(6, 7, 2, 1, 0)
maior(-12, 8, 3, 1, 112, 8,)
maior(40, 42, 44, 49)
maior(9)
maior(-12, -15, -18)
maior()
