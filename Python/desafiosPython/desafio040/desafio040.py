n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2)/2
if media < 5:
    print(f'Sua média foi {media:.1f}. Você foi REPROVADO!')
elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media:.1f}. Você ficou em RECUPERAÇÃO!')
elif media >= 7:
    print(f'Sua média foi {media:.1f}. Você está APROVADO!')