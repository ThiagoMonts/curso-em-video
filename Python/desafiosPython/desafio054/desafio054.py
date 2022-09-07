from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range (1,8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if atual - nasc >= 18:
        maior += 1
    else:
        menor += 1
print(f'Das {c} pessoas ouvidas, {maior} são maiores de idade e {menor} são menores de idade.')