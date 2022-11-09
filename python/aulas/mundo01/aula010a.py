'''nome = str(input('Qual o seu nome?'))
if nome == 'Thiago':
    print('Que nome bonito você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')'''

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('DIgite a sua segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
#if m >= 6.0:
#    print('A sua média foi boa. Parabéns!')
#else:
#    print('A sua média foi ruim. ESTUDE MAIS!')
print('PARABÉNS!' if m>=6 else 'ESTUDE MAIS!')