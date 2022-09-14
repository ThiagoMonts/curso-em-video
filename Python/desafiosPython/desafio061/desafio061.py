print('='*25)
print('GERADOR DE PA')
print('='*25)
n = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
c = 0
while c < 10:
    print(n, end=' -> ')
    n += razão
    c += 1
print('Fim!')