resp = 'S'
soma = quant = media = maior = menor = 0
maior = 0
menor = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}.')
print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}.')
