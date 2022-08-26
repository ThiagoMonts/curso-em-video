print('{:=^40}'.format(' LOJA DO MONTS '))
preco = float(input('Preço das compras: R$ '))
print('''Formas de Pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a sua opção? '))

if opção == 1:
    total = preco - (preco*10/100)
elif opção == 2:
    total = preco - (preco*5/100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.')
elif opção == 4:
    total = preco + (preco *20/100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R$ {parcela:.2f} COM JUROS.')
else:
    total = 0
    print('Opção inválida de pagamento. Tente novamente!')
print(f'Sua compra de R$ {preco:.2f} vai custar R$ {preco:.2f} no final.')