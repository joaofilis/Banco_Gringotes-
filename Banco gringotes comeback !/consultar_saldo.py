def consul_sal ():
    senha_cad = 1234
    saldo = 1000
    senha = int(input('Digite sua senha: '))
    if senha == senha_cad:
        print('Seu saldo atual é R${:.2f}'.format(saldo))
    else:
        print('Senha incorreta!')