peso = float(input('Qual o seu peso: (Kg) '))
altura = float(input('Qual a sua altura: (m) '))
IMC = peso / altura ** 2
print(f'Seu IMC é igual a {IMC:.1f}, ',end='')
if IMC < 18.5:
    print('você está abaixo do peso.')
elif IMC < 25:
    print('você está no peso ideal.')
elif IMC < 30:
    print('você está com sobrepeso.')
elif IMC < 40:
    print('você está obeso.')
else:
    print('você está com obesidade mórbida.')