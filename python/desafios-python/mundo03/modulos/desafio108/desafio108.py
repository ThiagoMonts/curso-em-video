from moeda import *
p = float(input('Digite o preço: R$ '))
print(f'A metade do {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p, 10))}')
print(f'Diminuindo 10%, temos {moeda(diminuir(p, 10))}')