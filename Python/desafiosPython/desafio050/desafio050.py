s = 0
cont = 0
for c in range (1,7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'Você informou {cont} valores pares e a soma deles é igual a {s}.')