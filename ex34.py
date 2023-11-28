print('-' * 15, 'CALCULADORA DE AUMENTO', '-' * 15)
sal = float(input('Digite o salário: R$ '))
if sal > 1250:
    Nsal = sal + (sal * 10/100)
else:
    Nsal = sal + (sal * 15/100)
print('O novo salário do funcionário é de: R${}'.format(Nsal))
