from datetime import date
#MAIORIDADE COMO 21 ANOS
anoAtual = date.today().year
contMaior = 0
contMenor = 0
for c in range(1, 8, 1):
    anoNasc = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = (anoAtual - anoNasc)
    if (idade >=21):
        contMaior += 1
    else:
        contMenor += 1
print('A quantidade de maiores de idade é: {}'.format(contMaior))
print('A quantidade de menores de idade é: {}'.format(contMenor))
