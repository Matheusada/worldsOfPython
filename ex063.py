print('{:-^25}'.format('FIBONACCI'))
print('=-'*15)
t1 = 0
t2 = 1
n = int(input('Digite: '))
print(t1,t2, end=' ')
cont = 3 #TIRANDO OS 2 T1 E T2/SOLUÇÃO MAIS ELEGANTE
while cont <= n:
    cont += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end=' ')
print('FIM!')
