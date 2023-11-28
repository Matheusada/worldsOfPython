r1 = str(input('Digite a 1ª reta que deseja formar o triângulo: ')).strip()
r1 = len(r1)
r2 = str(input('Digite a 2ª reta que deseja formar o triângulo: ')).strip()
r2 = len(r2)
r3 = str(input('Digite a 3ª reta que sdeseja formas o triângulo: ')).strip()
r3 = len(r3)

if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1:
    print('Essas retas NÃO podem formar um triângulo!')
else:
    print('As retas digitadas podem formar um triângulo!')