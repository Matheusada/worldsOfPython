import random
numeroPc = random.randint(0,10)
numeroUsu = int(input('Tente acertar o número sorteado pelo PC: '))
tentativas = 0
if numeroPc == numeroUsu:
    print('PARABÉNS, VOCÊ PRECISOU DE 1(UMA) TENTATIVA PARA ACERTAR !')
while numeroPc != numeroUsu:
    tentativas += 1
    if numeroPc < numeroUsu:
        numeroUsu = int(input('ERROUUU ! Tente novamente! Digite outro número MENOR: '))
    if numeroPc > numeroUsu:
        numeroUsu = int(input('ERROUUU ! Tente novamente ! Digite outro número MAIOR: '))
if numeroPc == numeroUsu and tentativas > 0:
    print('ÓTIMO, VOCÊ PRECISOU DE {} TENTATIVAS PARA ACERTAR'.format(tentativas + 1))
