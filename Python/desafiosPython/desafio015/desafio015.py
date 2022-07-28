dias = int(input('Por quantos dias o carro foi alugado? '))
distancia = float(input('Quantos Km rodados? '))
print(f'O total a pagar é de R$ {(dias*60) + (distancia*0.15):.2f}')