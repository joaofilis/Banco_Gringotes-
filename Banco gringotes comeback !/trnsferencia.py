def transf():
    saldo = 1000
    valor_transf = int(input('Digite o valor da transferência: '))
    cliente_nome = str(input('Digite o nome do cliente: '))
    nome_banco = str(input('Digite o nome do banco: '))
    agency_transf = int(input('Digite o N° da agência: '))
    conta_transf = int(input('Digite o N° da conta: '))
    if saldo >= valor_transf:
        print('Operação realizada com sucesso!')
        saldo = (saldo-valor_transf)
        print('O seu saldo é de R${:.2f}'.format(saldo))
    else:
        print('Operação não realizada o seu saldo é insuficiente ')
        print('O seu saldo é de R${:.2f}'.format(saldo))