from moeda import *
p = float(input('Digite o preço: R$ '))
print(f'A metade do R$ {p} é R$ {metade(p)}')
print(f'O dobro de R$ {p} é R$ {dobro(p)}')
print(f'Aumentando 10%, temos R$ {aumentar(p, 10)}')
print(f'Diminuindo 10%, temos R$ {diminuir(p, 10)}')