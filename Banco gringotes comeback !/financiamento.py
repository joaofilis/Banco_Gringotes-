def finan():

    i = 0
    tot_renda = 0
    print('Ok mas antes de financiar preciso de algumas informações')
    pess_rend = int(input('Quantas pessoas possuem renda na sua casa?'))
    while pess_rend > i: #tem que usar 'for' porque se não fica no looping infinito
        rend_familia = int(input('Valor da renda do membro:'))
        tot_renda = (tot_renda + rend_familia) #nesta linha enquanto esta dentro do while o programa vai somando a renda dos familiares
        temp_serv = int(input('Quanto tempo de serviço você tem ?: '))
    print('O total de renda familiar é R${:.2f}'.format(tot_renda))

    print('Bem vindo ao financiamento online (cuidado com o que você coloca neste campo meu jovem)')
    #no caso abaixo eu não sei trabalhar muito bem com booleanos mas vou tentar usar neste caso para o if
    print('O que você pretende financiar?')
    print('{1} - Imóveis  {2} - Automóveis  {3} - Nada vim aqui por engano')
    escolha = int(input('Bora rapaz diga: '))

    if (escolha == 1) or (escolha == 2):
        val_fin = int(input('Digite o valor do Financiamento: '))
        val_entrada = int(input('Digite o valor de entrada: '))
        temp_fin = int(input('Digite o tempo de financiamento: '))
        tot_fin = ((val_fin-val_entrada)* 1.8) #calculo juros do financiamento
        val_par = (tot_fin/temp_fin)  #calculo valor da parcela
        rend = ((tot_renda*40)/100)   #calculo porcentagem renda familiar
        val_tot = (val_fin - val_entrada)  #calculo falor do financiamento
        if (tot_fin < rend) or (temp_serv <= 3):
            print('Valor de financiamento não aprovado pelo sistema')
        elif (tot_fin > rend) or (temp_serv > 3):
            print('Parabéns o Banco Gringotes aprova o seu financiamento!')
        else:
            print('Algo no seu financiamento está errado')
    else:
        print('Obrigado por utilizar o Banco Gringotes')