num = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha a opção para conversão:\n[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3]converter para HEXADECIMAL\nSua opção:'))
if opcao == 1:
    print('Convertendo o número {} para BINÁRIO, temos {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('Convertendo o número {} para OCTAL, temos {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('Convertendo o número {} para HEXADECIMAL, temos {}'.format(num, hex(num)[2:]))
else:
    print('Por favor, digite um valor CORRETO \n'
          'ENCERRANDO PROGRAMA...')



