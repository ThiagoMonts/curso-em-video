somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for p in range (1,5):
    print(f'------{p}ª PESSOA------')
    nome = str(input(f'Nome: ').strip())
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ').strip())
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}.')
print(f'Ao todo são {totMulher20} mulheres com menos de 20 anos.')