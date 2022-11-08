from moeda import *
p = float(input('Digite o preço: R$ '))
print(f'A metade do {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10%, temos {aumentar(p, 10, True)}')
print(f'Diminuindo 10%, temos {diminuir(p, 10, True)}')