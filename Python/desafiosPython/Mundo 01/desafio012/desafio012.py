preco = float(input('Qual o preço do produto? R$ '))
print(f'O produto que custava {preco}, na promoção com desconto de 5% vai passar a custar R$ {preco - (preco*5/100):.2f}')