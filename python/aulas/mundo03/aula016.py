#No Python eu posso começar uma variavel composta de 3 maneiras () = tupla [] = lista {} = dicionário
#Lembrando que as tuplas são IMUTÁVEIS!
#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#print(lanche[1]) #Irá mostrar Suco, pois a contagem começa do 0
#print(lanche[-2]) #Irá mostrar Pizza, pois o menos serve para mostrar do final para o inicio, o último item é -1
#print(lanche[1:3]) #Irá mostrar a partir do item na posição 1 (Suco) até o 3, lembrando que desconsidera o último número, portanto irá mostrar Pizza
#print(lanche[2:]) #Irá mostrar do elemento 2 até o final
#print(lanche[:2]) #Irá mostrar do começo até o elemento 2, como ignora o último, vai mostrar até Suco
#print(lanche[-2:]) #Irá começar na pizza e vai até o final
#print(lanche) #Irá mostrar a tupla inteira
#lanche[1] = 'Refrigerante' #Esse comando não será executado pois as tuplas são IMUTÁVEIS

#for comida in lanche: #Essa forma é usada se eu não precisar mostrar a posição
#    print(f'Eu vou comer {comida}')

#for pos, comida in enumerate(lanche): #Irá fazer um laço mostrando todas as comidas,  uma de cada vez
#    print(f'Eu vou comer {comida} na posição {pos}')
#print('Comi pra caramba')

#for cont in range(0, len(lanche)): #Essa forma ou a de cima darão o mesmo resultado. Se precisar mostrar a posição tem que ser dessa forma ou na de cima com o enumerate
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #Irá mostrar todas as comidas

#for cont in range(0, len(lanche)):
#    print(cont) #Irá mostrar apenas o indice, no caso, 0, 1, 2, 3

#print(len(lanche)) #Irá mostrar que eu tenho 4 comidas, são 4 itens na tupla.
#Se o programa tá parado eu posso mexer na tupla, só não posso mexer se o programa estiver em execução

#print(sorted(lanche)) #Irá mostrar em ordem

#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a+b #Se eu faço essa operação, irá juntar a tupla a com a tupla b
#c = b+a #Lembrando que a ordem irá interferir nesse caso
#print(c)
#print(len(c)) #Irá mostrar a quantidade de elementos, no caso 7 elementos, 3 de a e 4 de b
#print(c.count(5)) #Nesse caso irá mostrar quantas vezes o número 5 aparece dentro da tupla
#print(c)
#print(c.index(8)) #Irá mostrar em que posição está o número 8, lembrando que sempre começa pelo 0
#print(c.index(2)) #Apesar do número 2 aparecer 2x, ele vai pegar da primeira ocorrência
#print(c.index(5,1)) #Irá procurar quando aparece o número 5 após da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88) #No Python eu posso ter tipos diferentes dentro das tuplas
del(pessoa) #Nesse caso eu apago da memória a tupla toda
print(pessoa)
