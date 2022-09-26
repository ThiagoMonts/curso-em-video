times = ('Corinthians', 'Santos', 'Avaí', 'América-MG', 'Bragantino',
          'Atlético-MG', 'São Paulo', 'Botafogo', 'Internacional', 'Coritiba',
          'Cuiabá', 'Athletico-PR', 'Palmeiras', 'Flamengo', 'Fluminense',
          'Goiás', 'Ceará', 'Juventude', 'Atlético-GO', 'Fortaleza')
print('=-'* 20)
print(f'Lista de times do Brasileirão: {times}')
print('=-'* 20)
print(f'Os 5 primeios são: {times[0:5]}')
print('=-'* 20)
print(f'Os 4 últimos são: {times[-4:]}')
print('=-'* 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'* 20)
print(f'O Flamengo está na posição {times.index("Flamengo")+1}ª da tabela')
