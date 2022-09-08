maior = 0
menor = 0
for p in range (1,6):
    peso = float(input(f"Peso da {p}ª pessoa (Kg): "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MAIOR peso lido foi {maior}Kg.')
print(f'O MENOR peso lido foi {menor}Kg.')
