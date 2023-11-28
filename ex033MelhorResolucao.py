a = float(input('Digite o 1ª número:'))
b = float(input('Digite o 2º número: '))
c = float(input('Digite o 3ª número: '))
#VERIFICANDO O MAIOR (COLOCANDO UM DELES COMO MAIOR, PARA JÁ ELIMINAR UMA INSTÂNCIA DE 'IF'
maiorN = a
if b > a and b > c:
    maiorN = b
if c > a and c > b:
    maiorN = c
#VERIFICANDO O MENOR(COLOCANDO UM DELES COMO MENOR, PARA JÁ ELIMINAR UMA INSTÂNCIA DE 'IF'
menorN = a
if b < a and b < c:
    menorN = b
if c < a and c < b:
    menorN = c
print('O maior valor digitado foi: {}'.format(maiorN))
print('O menor valor digitado foi: {}'.format(menorN))
