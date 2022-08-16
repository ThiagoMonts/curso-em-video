salario = float(input('Qual o salário do funciónario? R$: '))
if salario > 1250.00:
    print(f'O novo salário será de R$ {salario + (salario*10/100)}, com os 10% de aumento.')
else:
    print(f'O novo salário será de R$ {salario + (salario*15/100)}, com os 15% de aumento.')