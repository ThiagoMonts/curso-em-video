r1 = float(input('Qual o comprimento do primeiro segmento? '))
r2 = float(input('Qual o comprimento do segundo segmento? '))
r3 = float(input('Qual o comprimento do terceiro segmento? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Não é possível formar um triângulo')