'''def teste(b):
    a = 8
    b+=4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a=5
teste(a)
print(f'A fora vale {a}')'''


'''def teste(b):
    global a
    a = 8
    b+=4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a=5
teste(a)
print(f'A fora vale {a}')'''




'''def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa principal
n = 2 #O n tem escopo global
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}')
# #Vai dar erro, pois o x só foi definido dentro da função, portanto tem escopo local'''

'''n1 = 2
print(f'N1 global vale {n1}')'''

'''def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
função()
print(f'N1 fora vale {n1}')'''

#Explicando o retorno
'''def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(2,2)
somar(6)'''

'''def somar(a=0,b=0,c=0):
    s = a+b+c
    return s


resp = somar(3, 2, 5) #Posso jogar a resposta da soma acima, dentro de uma variável, nesse caso, 'resp'''''

'''def somar(a=0,b=0,c=0):
    s = a+b+c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)

print(f'Meus cálculos deram {r1}, {r2} e {r3}.')'''

'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1): #Irá começar no número e vai até 0, voltando de 1 em 1
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''


'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1): #Irá começar no número e vai até 0, voltando de 1 em 1
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(1)
print(f'Os resultados são {f1}, {f2} e {f3}.')'''

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
