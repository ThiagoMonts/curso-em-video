#teste = list()
#teste.append('Gustavo')
#teste.append(40)
#galera = list()
#galera.append(teste) #Nesse caso eu estou criando uma ligação entre as duas estruturas, elas ficarão iguais
#galera.append(teste[:]) #Para evitar que ocorra a ligação, tenho que fazer uma cópia, usando o [:]
#print(galera) #Nesse caso irá mostrar, ['Gustavo', 40] dentro de outra lista
#teste[0] = 'Maria' #Estou indicando que quero mudar o item 0 de teste, trocando Gustavo por Maria
#teste[1] = 22 #Estou indicando que quero mudar o item 1 de teste, trocando 40 por 22
#galera.append(teste)
#galera.append(teste[:]) #Para evitar que ocorra a ligação, tenho que fazer uma cópia, usando o [:]
#print(galera)

#galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera) #Irá mostrar todos os itens
#print(galera[0]) #Irá mostrar apenas o primeiro item, no caso, ['João', 19]
#print(galera[0][0]) #Irá mostrar apenas o primeiro item de galera 0, no caso 'João'
#print(galera[2][1]) #Irá mostrar o item 2 de galera e o item 1 dentro dele, no caso 13
#for p in galera:
    #print(p) #Irá mostrar todos os nomes com suas respectivas idades, separados
    #print(p[0]) #Irá mostrar apenas os nomes
    #print(p[1]) #Irá mostrar apenas as idades
    #print(f'{p[0]} tem {p[1]} anos de idade') #Irá mostrar todos os nomes com suas respectivas idades formatados

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3): #Estrutura de repetição, irá pedir o nome e idade 3 vezes
    dado.append(str(input('Nome: '))) #Irá adicionar os nomes na lista dado
    dado.append(int(input('Idade: '))) #Irá adicionar as idades na lista dado
    galera.append(dado[:]) #Irá copiar a lista dado para a lista galera
    dado.clear() #Irá apagar a lista dado. Se eu não fizer isso que fiz acima (copiar [:]), irá gerar uma lista vazia
#print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
