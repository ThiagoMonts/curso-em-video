n = int(input('Digite um número [999 para parar]: '))
cont = 0
soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Foram digitados {cont} números e a soma entre eles é igual a {soma}.')