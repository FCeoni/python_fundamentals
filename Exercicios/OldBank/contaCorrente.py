#  OldBank - contaCorrente.py

#
# import os
# from time import time

# os.system('clear')

# def opcaoInicial():
#     print("\n\n===============  Bem vindo ao Old Bank! =================")
#     print('\n===============   MENU PRINCIPAL   ======================\n')
#     print("Escolha sua opção: \n \t1- Abrir Conta Corrente\n \t2- Movimentar Conta Corrente\n\t0 - Sair")
#     opcaoInicial = int(input("\t>>> "))

#     try:
#         if opcaoInicial == 1:
#             menuAbertura()
#         elif opcaoInicial == 2:
#             menuMovimenta()
#         elif opcaoInicial == 0:
#             print(" Até Breve!")
#             sleep(3)
#             os.system('clear')
#             exit()
#         else:
#             raise ValueError("Opção Inválida")
#     except ValueError as m1:
#         print(m1)
#     print(f"\nOpção selecionada  < {opcaoInicial} >")

# def menuAbertura():
#     os.system('clear')
#     print("\n\n===============  Bem vindo ao Od Bank! =================")
#     print('\n==========  ABERTURA DE CONTA CORRENTE ==================\n')
 #   print("Entre com as informações abaixo: \n \t \            a \ no final dá continuidade ao string na linha posterior
 #       1-Digite seu nome completo:\n \t \
 #       2- Difgite o valor do depósito inicial: \n")
    # nomeCorrentista = str(input(" \tDigite seu nome completo >>>"))
    # valorInicial = int(input(" \tValor do Depósito Inicial >>> R$ "))
    
# try:
#     if opcaoInicial == 1:
#         menuAbertura()
#     elif opcaoInicial == 2:
#         menuMovimenta()
#     else:
#         raise ValueError("Opção Inválida")
# except ValueError as m1:
#     print(m1)
# print(f"Opção selecionada: {opcaoInicial}")

# def menuMovimenta():
#     print("Escolha sua opção: \n \t1- Abrir Conta Corrente\n \t2- Movimentar Conta Corrente\n")
#     opcaoInicial = int(input(">>> "))

# try:
#     if opcaoInicial == 1:
#         menuAbertura()
#     elif opcaoInicial == 2:
#         menuMovimenta()
#     else:
#         raise ValueError("Opção Inválida")
# except ValueError as m1:
#     print(m1)
# print(f"Opção selecionada: {opcaoInicial}")

# class contaCorrente (self):
#     self.idBanco = 999
#     self.numCCorrente = None
#     self.numAgencia = '08'
#     self.nomeCliente = None
#     self.valorSaldo = None
#     self.valorMovimento = None
    
#     def Depositar(self, numCCorrente, numCCorrente, numAgencia, valorMovimento):
#         pass



#     def Sacar(self, numCCorrente, numCCorrente, numAgencia, valorMovimento):
#         pass



#     def Saldo(self, numCCorrente, numCCorrente, numAgencia, valorMovimento):
#         pass

# opcaoInicial()


from datetime import datetime

class Oldbank():
    """ Classe responsavel pela movimentacao da conta"""

    def __init__(self):
        self.numeroBanco = '999'
        self.numeroAg = '08'
        self.nomeCliente = None
        self.conta = 9991
        self.saldo = 0

    def cria_conta(self):
        print('Bem Vindo(a) ao sistema de criação de conta!')
        nome = input('Digite seu nome: ')
        self.nomeCliente = nome
        self.conta += 1
    
    def depositar(self):
        self.deposito = int(input('Digite o valor de deposito: '))
        if self.deposito > 0:
            self.saldo += self.deposito
        else:
            print('Valor Inválido')
    
    def sacar(self):
        self.saque = int(input('Digite o valor de saque: '))
        if self.saque < self.saldo:
            self.saldo -= self.saque
        else:
            print('Saldo Insuficiente')

    def extrato(self):
        print(f'Data e Hora da consulta: {datetime.now()}')
        print(f'-'*20)
        print(f'Ag: {self.numeroAg} Conta: {self.conta}')
        print(f'Cliente: {self.nomeCliente}')
        print(f'Saldo atual: {self.saldo}')

