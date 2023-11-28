#Programa que leia nome completo da pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras, sem considerar espaços
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print('Nome com todas as letras Maiúsculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('O número de letras do nome digitado, sem contar os espaços é:{}'.format (len(nome.strip().replace(" ",""))))
nome = nome.split()
print('O primeiro nome digitado: {}, tem {} letras'.format(nome[0], len(nome[0])))
#print('Sem considerar os espaços, o nome possui: {} letras'.format(nome.count()))
#print('O primeiro nome tem: {} letras'.format)