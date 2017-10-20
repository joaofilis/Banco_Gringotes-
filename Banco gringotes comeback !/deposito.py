def deposito():
    saldo = 1000
    val_dep = int(input('Digite o valor do depósito: '))
    agency_deposito = int(input('Digite o N° da agência: '))
    conta_dep = int(input('Digite o N° da conta: '))
    saldo = (saldo + val_dep)
    print('o seu saldo é de R${:.2f}'.format(saldo))
