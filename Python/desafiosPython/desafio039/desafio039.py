from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
sexo = str(input('''Qual o seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino
Sua opção: '''))

if sexo == '1':
    print(f'Quem nasceu em {nasc} tem {idade} de idade em {atual}.')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!!!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Você ainda não tem 18 anos, ainda faltam {saldo} anos para o alistamento.')
        ano =  atual + saldo
        print(f'Seu alistamento será em {ano}.')
    else:
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano}.')
elif sexo == '2':
    print('Você não precisa se alistar!')
