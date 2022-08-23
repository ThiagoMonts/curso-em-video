from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print(f'Sua categoria será a MIRIM.')
elif idade <= 14:
    print(f'Sua categoria será a INFANTIL.')
elif idade <= 19:
    print(f'Sua categoria será a JÚNIOR.')
elif idade <= 25:
    print(f'Sua categoria será a SÊNIOR.')
else:
    print(f'Sua categoria será a MASTER.')