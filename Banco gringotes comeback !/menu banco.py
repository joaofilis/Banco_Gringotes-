#Este file é uma recriação do banco gringotes feito na unifieo para mero aprendizado e treinamento em python
from consultar_saldo import consul_sal 
from deposito import deposito 
from financiamento import finan
from saque import saque 
from trnsferencia import transf
print('Bem vindo ao Banco Gringotes!')
#terminar a estrutura while
cad = str(input('Você possue cadastro?:'))
if (cad == ('sim')):
    print('Bem vindo de volta João ao Banco Gringotes!')
    print('MENU INICIAL')
    print('{1} - CADASTRO \n{2} - DEPÓSITO  \n{3} - SAQUE \n{4} - CONSULTAR SALDO \n{5} - TRANSFERÊNCIA \n{6} - FINANCIAMENTO \n{7} - SAIR DO SISTEMA ')
    resposta= int (input('Escolha uma opção acima: '))
    if(resposta == 1):
        print('Preguiçoso')
    elif(resposta == 2):
        deposito()
    elif(resposta == 3):
        saque()
    elif(resposta == 4):
        consul_sal()
    elif(resposta == 5):
        transf()
    elif(resposta == 6):
        finan()
    elif(resposta == 7):
        print('Obrigado por utilizar o Banco Gringotes!')

elif (cad == ('nao')):
    print('Gostaria de realizar cadastro?')
    print('Digite suas informações aqui')
    nome = str(input('Digite seu nome: '))
    end = str(input('Digite seu endereço: '))
    num_casa = int(input('Digite o número da casa: '))
    city = str(input('Digite o nome da cidade: '))
    birthday = int(input('Digite sua data de Nascimento: '))
    CPF = int(input('Digite seu CPF: '))
    RG = int(input('Digite seu RG: '))
    empresa = str(input('Digite o nome da empresa em que você trabalha: '))
    sal = int(input('Digite seu salário: '))
    tempo = int(input('Digite há quanto tempo você trabalha na {}'.format(empresa)))
    senha_cad = str(input('Digite uma senha: '))
    agency = int(input('Digite a agência mais próxima: '))
    #como fazer para colocar o número na conta (pegar a aula do guanabara que gera um valor aleatório)
    saldo = int(input('Digite o saldo inicial:'))
    #AINDA TEM COISA PARA COLOCAR AQUI
else:
    i = 0
    print('Comando não reconhecido!')
    print('O programa não irá executar bye!')
