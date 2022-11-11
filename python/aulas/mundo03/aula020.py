'''def lin():
    print('-'*30)


#Programa principal
lin()
print(f'{"CURSO EM VÍDEO":^30}')
lin()
print(f'{"APRENDA PYTHON":^30}')
lin()
print(f'{"GUSTAVO GUANABARA":^30}')
lin()'''


'''def título(txt):
    print('-'*30)
    print(txt)
    print('-' * 30)


#Programa principal
título('CURSO EM VÍDEO')
título('APRENDA PYTHON')
título('GUSTAVO GUANABARA')'''


'''a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
#Posso substituir tudo isso acima por essa função abaixo.
def soma(a, b):
    soma = a + b
    print(soma)


#Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
#soma(4) # Irá dar erro, pois na minha função eu determinei que serão 2 parâmetros
soma(a=4, b=5) #Posso mudar a ordem, sem problema'''


'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


#Programa principal
soma(b=4,a=5)
soma(7, 2) #Se eu não explicitar, o programa entende que o primeiro parâmetro é 'a' e o segundo é 'b'
'''

'''def contador(* num):
    print(num)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''def contador(* num):
    for valor in num:
        print(valor, end=' ')
    print('FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''


'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''


'''def dobra(lst):
    pos = 0
    while pos < len(lst): #Enquanto a posição for menor que o tamanho da lista
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''


def soma(* valores):
    s= 0
    for num in valores: #Para cada número em valores
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)