l = float(input('Qual a largura da parede (em metros): '))
a = float(input('Qual a altura da parede (em metros): '))
print(f'Sua parede tem a dimensão de {l}m x {a}m e sua área é de {l*a:.2f}m².')
print(f'Para pintar essa parede, você precisará de {(l*a)/2:.2f}l de tinta.')