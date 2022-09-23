total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Produto: '))
    valor = float(input('Valor R$: '))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O valor total gasto na compra foi R$ {total:.2f}.')
print(f'A quantidade de produtos acima de R$ 1000.00 foi {totmil}.')
print(f'O produto mais barato foi {barato} e custou R$ {menor:.2f}.')