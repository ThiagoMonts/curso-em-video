''' //Solução com importação:
from math import hypot
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoOposto,catetoAdjacente)
print(f'Se o cateto oposto for {catetoOposto} e o cateto adjacente for {catetoAdjacente}, a hipotenusa irá medir {hipotenusa:.2f}.')'''

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print(f'Se o cateto oposto for {catetoOposto} e o cateto adjacente for {catetoAdjacente}, a hipotenusa irá medir {hipotenusa:.2f}.')