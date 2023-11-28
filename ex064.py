n = int(input('Digite o número: '))
num = cont = soma = 0
while n != 999:
    n = int(input('Digite o número:'))
    cont += 1
    soma += n
    n = int(input('Digite o número: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont,soma))
