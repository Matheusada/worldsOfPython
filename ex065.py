resp = 'S'#Aquer continuar ?
soma = cont = 0
while resp == 'S': # Outra forma, while resp in 'Ss'
    n = int(input('Digite o valor: '))
    cont += 1
    soma += n
    if cont == 1:
        maiorValor =  menorValor = n
    else:
        if n >= maiorValor:
            maiorValor = n
        if n < menorValor:
            menorValor = n
    resp = str(input('Deseja continuar digitando valores ? [S/N]')).upper().strip()[0] # [0] para considerar apenas 1ª letra
print('Encerrando Programa...\nO Maior valor digitado foi {}'.format(maiorValor))
print('O MENOR valor digitado foi {}'.format(menorValor))
print('A MÉDIA dos valores digitado foi {}'.format(soma/cont))



