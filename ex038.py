n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('O número {} é maior que o {}'.format(n1, n2))
elif n1 < n2:
    print('O número {} é menor que o {}'.format(n1, n2))
else:
    print('Os dois números são IGUAIS')
