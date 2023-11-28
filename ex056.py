#PROGRAMA - NOME, IDADE, SEXO de 4 pessoas / NOME DO HOMEM MAIS VELHO / QUANTAS MULHERES TEM MENOS DE 20 ANOS !
print('{:%^60}'.format(' LEITOR DE NOME IDADE E SEXO- 4 PESSOAS '))
homemVelho = ''
mAbVinte = 0
somaIdade = 0
idadeVelho = 0
for pessoa in range(1, 5, 1):
    #LENDO NOME IDADE E SEXO
    nome = str(input('Digite o \033[1;031mNOME\033[m da {}ª pessoa: '.format(pessoa))).strip()
    idade = int(input('Digite a \033[1;032mIDADE\033[m da {}ª pessoa: '.format(pessoa)))
    sexo = str(input('Digite o \033[1;033mSEXO\033[m (M/F) da {}ª pessoa: '.format(pessoa))).upper().strip()
    #MEDIA IDADE
    somaIdade += idade
    if sexo == 'F' and idade < 20:
        mAbVinte += 1
    #HOMEM MAIS VELHO
    if pessoa == 1 and sexo == 'M': #alternativa and sexo in 'Mm' (mesma coisa)
        homemVelho = nome
        idadeVelho = idade
    if sexo == 'M' and idade > idadeVelho:
        homemVelho = nome
        idadeVelho = idade

print('A média das idades é de {}'.format(somaIdade/4))
print('São {} as mulheres com MENOS de 20 anos'.format(mAbVinte))
print('O nome do homem mais velho é {}, com {} anos'.format(homemVelho, idadeVelho))



