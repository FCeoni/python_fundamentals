import os
from time import sleep
from contaCorrente import Oldbank


def main():
    conta = Oldbank()
    while True:
        print('-------OldBank-------')
        print('Bem vindo(a)!')
        print('Selecione a opção abaixo:')
        print('Para Criar Conta, Digite 1')
        print('Para Deposito, Digite 2')
        print('Para Saque, Digite 3')
        print('Para Extrato, Digite 4')
        print('Para Sair, Digit 0')
        opcao = int(input('>>> '))
        if opcao == 1:
            os.system('clear')
            conta.cria_conta()
            continue
        elif opcao == 2:
            os.system('clear')
            conta.depositar()
            conta.extrato()
            sleep(2)
            continue
        elif opcao == 3:
            os.system('clear')
            conta.sacar()
            conta.extrato()
            sleep(2)
            continue
        elif opcao == 4:
            os.system('clear')
            conta.extrato()
            sleep(2)
            continue
        elif opcao == 0:
            exit()
        else:
            print('Opção Invalida')

main()