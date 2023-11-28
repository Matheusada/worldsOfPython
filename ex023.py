number = str(input('Digite um número entre 0 a 9999: '))
n = int(number)
if n < 0 or n > 9999:
    print('Atenção!!!!Digite um valor válido!!!')
if len(number) == 4:
    print(number[3])
    print(number[2])
    print(number[1])
    print(number[0])
elif len(number) == 3:
    print(number[2])
    print(number[1])
    print(number[0])
elif len(number) == 2:
    print(number[1])
    print(number[0])
else:
    print(number[0])


