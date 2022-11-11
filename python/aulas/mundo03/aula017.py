#num = [2,5,9,1] #Diferentemente da tupla, na lista eu posso substituir os valores
#num[2] = 3 #Nesse caso, o valor 3 irá substituit o 9 que está na posição [2]
#num[4] = 7 #Eu não posso adicionar valores dessa forma, já que não existe um item na posição 4
#num.append(7) #Essa é a forma correta de adicionar um elemento.
#num.sort() #Irá colocar a lista em ordem
#num.sort(reverse=True) #Nesse caso a lista será ordenada de forma decrescente
#num.insert(2,0) #Irá inserir um valor na posição indicada, nesse caso irá inserir o 0 na posição 2
#num.pop() #Irá eliminar o último elemento, se não for indicado qual você deseja eliminar
#num.pop(2) #Irá eliminar o elemento na posição 2, no caso será o 0 que adicionei anteriormente
#num.insert(2,2)
#num.remove(4) #Se eu tentar remover um item que não tem na lista, irá acontecer um erro
#if 4 in num: #A solução quando não se sabe se o número está contido na lista é fazer a verificação com if
#    num.remove(4)
#else:
#    print('Não achei o número 4')
#num.remove(2) #Remove a primeira ocorrência do valor que você mandou eliminar
#print(num)
#print(f'Essa lista tem {len(num)} elementos') #Irá mostrar quantos elementos eu tenho na lista

#valores = list()
#valores.append(5)
#valores.append(9)
#valores.append(4)

#for v in valores: #Posso criar uma lista dessa forma, usando o for
#    print(f'{v}...', end='')

#for c, v in enumerate(valores): #Posso usar essa formatação para indicar a posição e o valor
#    print(f'Na posição {c} encontrei o valor {v}.')
#print('Cheguei ao final da lista')

#valores = list()
#for cont in range(0,5):
#    valores.append(int(input('Digite um valor: ')))
#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
#b = a #A partir do momento que eu faço isso, eu tô criando uma ligação entre as listas, o que eu mudar em uma, mudará na outra
b = a[:] #Nesse caso eu copio os elementos de a, não tem a ligação como aconteceu acima
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')