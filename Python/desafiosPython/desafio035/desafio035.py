print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = int(input('Qual tamanho do primeiro segmento? '))
r2 = int(input('Qual o tamanho do segundo segmento? '))
r3= int(input('Qual o tamanho do terceiro segmento? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')