print('='*25)
print('GERADOR DE PA')
print('='*25)
n = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print(n, end=' -> ')
        n += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')