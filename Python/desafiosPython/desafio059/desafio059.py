fim = False
num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
while not fim:
    escolha = int(input('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Qual é a sua opção: '''))
    if escolha == 1:
        print(f'A soma entre {num1} e {num2} é igual {num1+num2}.')
    elif escolha == 2:
        print(f'A multiplicação entre {num1} e {num2} é igual a {num1*num2}.')
    elif escolha == 3:
        if num1 > num2:
            print(f'O maior número entre {num1} e {num2} é {num1}.')
        else:
            print(f'O maior número entre {num1} e {num2} é {num2}')
    elif escolha == 4:
        print('Informe os números novamente:')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite mais um número: '))
    elif escolha == 5:
        break
    else:
        print('Opção inválida. Tente novamente.')
    print('-='*20)
print('Fim do programa')