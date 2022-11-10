nome = str(input('Qual o seu nome? '))
if nome == 'Thiago':
    print('Que nome bonito!')
elif nome == 'Tatiana' or nome == 'Vanessa' or nome == 'João':
    print('O seu nome é bem poupular no Brasil!')
elif nome in 'Pedro Thalyson':
    print('Belo nome masculino')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')