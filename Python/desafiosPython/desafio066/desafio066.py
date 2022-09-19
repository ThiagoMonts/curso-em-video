cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'O total de números digitados foi {cont}.')
print(f'A soma de todos os números digitados é igual a {soma}.')