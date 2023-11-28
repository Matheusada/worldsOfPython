sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Digite corretamente')
    sexo = str(input('Informe o seu sexo [M/F]: ')).upper().strip()
print('Sexo {} registrado com SUCESSO'.format(sexo))