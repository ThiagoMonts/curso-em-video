valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual é o seu salário atual? R$ '))
anos =  int(input('Em quantos anos você pretende pagá-la? '))
prestação = valor / (anos *12)
print(f'Para pagar uma casa de R$ {valor:.2f} em {anos} anos, a prestação será de R$ {prestação:.2f} por mês.')
if prestação > salario*30*100:
    print('Seu empréstimo foi negado!')
else:
    print('Parabéns! Seu empréstimo foi aprovado!')