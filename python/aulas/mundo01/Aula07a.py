#nome = input('Qual o seu nome?')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, a multiplicação é {}, a divisão é {:.2f}'.format(s,m,d))
print('A divisão inteira é {}, a potência é {}'.format(di,e))