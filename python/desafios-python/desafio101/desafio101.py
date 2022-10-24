def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif idade <= 18 or idade >= 65:
        return f'Com {idade} anos: VOTO FACULTATIVO.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


#Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))