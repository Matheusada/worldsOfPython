#VERIFICADOR DE PALÍNDROMO
frase = str(input('Digite a frase para verificação: ')).lower().split()
frase = ''.join(frase).strip()
print(frase)
inverso = ''
for c in range(len(frase)-1,-1,-1):
    inverso += frase[c]
print(inverso)
if frase == inverso:
    print('É PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO!')


