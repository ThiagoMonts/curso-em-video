while True:
    n = int(input('Que número você deseja saber a tabuada? '))
    print('-'*30)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('Programa Tabuada encerrado. Volte sempre!')