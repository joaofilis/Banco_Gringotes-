def saque():
    saldo = 1000
    saque = int(input('Digite o valor de saque: '))
    if saque > saldo:
        print('Saldo insuficiente operação não realizada!')
    else:
        saldo = (saldo - saque)
        print('Operação realizada com sucesso!')
        print('Seu saldo atualmente é de R${:.2f}'.format(saldo))

