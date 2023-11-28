print('*'*10, 'ANALISADOR DE MAIOR E MENOR NÚMERO', '*'*10)

n1 = float(input('Digite o 1ª número: '))
n2 = float(input('Digite o 2ªnúmero: '))
n3 = float(input('Digite o 3ª número: '))

if n1 > n2 and n2 > n3:
    maiorN = n1
    menorN = n3
elif n1 > n2 and n2 < n3:
    maiorN = n1
    menorN = n2
elif n2 > n1 and n1 > n3:
    maiorN = n2
    menorN = n3
elif n2 > n1 and n1 < n3:
    maiorN = n2

    menorN = n1
elif n3 > n1 and n1 > n2:
    maior = n3
    menor = n2
elif n3 > n1 and n1 < n2:
    maior = n3
    menor: n1

print('\nO MAIOR número digitado foi: {} e o MENOR foi: {}\n'. format(maiorN, menorN))
print('*'* 30)

