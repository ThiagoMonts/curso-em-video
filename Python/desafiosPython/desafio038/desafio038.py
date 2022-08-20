num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 == num2:
    print(f'Não existe valor maior, os dois números, {num1} e {num2}, são iguais.')
elif num1 > num2:
    print(f'O primeiro valor, {num1}, é maior que o segundo valor, {num2}.')
else:
    print(f'O segundo valor, {num2}, é maior que o primeiro valor, {num1}.')