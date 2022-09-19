print('='*25)
print('10 termos de uma PA')
print('='*25)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (11 - 1) * razão

for c in range (primeiro, décimo, razão):
    print(c, end=' -> ')
print('Acabou!')
