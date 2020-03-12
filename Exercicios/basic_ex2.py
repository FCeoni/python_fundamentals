import os

import sys

os.system('clear')

# curiosidades

# -*- coding: UTF-8 -*-    => para python2 reconhecer outros caracterers (não, exceção....)
# python --version
# from __future__ import print_function     para compatibilizar e verificar versoes no/do python   < _ _ double underscore = dundle > 
# venv/ativate

#====================================================================================================
# estruturas de repetição - While
#====================================================================================================

# x = 1

# # while < 10:
# #     print(x)            # x vai ser sempre < 10 => loop infinito


# # while True:
# #     print(x)
# #     x += 1
# #     print('new x =', x)     # loop infinito


# # while True:
# #     print(x)
# #     x += 1
# #     if x < 100:
# #         print('new x =', x)     # loop infinito
# #     else: 
# #         False

# # break

# # continue


# usuarios = dict(Renato='abacaxi123', Carlos='fusca123', Maria='teste321')

# bloqueados = []

# tentativas = 0

# while True:
#     login = input('Digite o seu usuário: ')
#     if login in usuários:
#         senha = input('Digite sua senha')
#         if senha == usuários[login]:            # default validação pela key, não por value.
#             print('Login efetuado com sucesso!')
#         elif tentativas < 4:
#             print('Credencial inválida!')
#             tentativas += 1
#             continue
#         else:
#             print('Credencial não cadastrada, Solicite ajuda do Administrador!')
#             bloqueados.append((login))
#             usuários.pop(login)
#             break

# print(f'usuários: {usuários}')
# print(f'usuários bloqueados: {bloquados}')


#====================================================================================================
# estruturas de repetição - For
#====================================================================================================

# frutas = ['banana', 'maça', 'uva']

# for f in frutas:
#     print(f)

# print('\n\n')

# for  i, f in enumerate(frutas):
#     print( i,  f)

# print('\n\n')


# usuarios = dict(Renato='abacaxi123', Carlos='fusca123', Maria='teste321')



# bloqueados = []
# tentativas = 0

# def login()
#     while True:
#         login = input('Digite o seu usuário: ')
#         if login in usuários:
#             senha = input('Digite sua senha')
#             if senha == usuários[login]:            # default validação pela key, não por value.
#                 print('Login efetuado com sucesso!')
#             elif tentativas < 4:
#                 print('Credencial inválida!')
#                 tentativas += 1
#                 continue
#             else:
#                 print('Credencial não cadastrada, Solicite ajuda do Administrador!')
#                 bloqueados.append((login))
#                 usuários.pop(login)
#                 break

# print(f'usuários: {usuários}')
# print(f'usuários bloqueados: {bloquados}')



#====================================================================================================
# erros e exceções  =>  try e except
#====================================================================================================

# ex_1

# while True:

#     try:
#         x = int(input('digite o primeiro numero: '))
#         y = int(input('digite o segundo numero: '))
#         print(x + y)
#         break
#     except ExeptionError as e:                          # Exception:  para erros genéricos
#         print(e.with_taceback())                        # geralmente utilizado para deploy debugging        
#         print(e)
#         continue
#     finally:
#         print('calculando....')                         # rodará independente do except


# ex_2

# try:
#     produto_id = [1111, 1112, 1113, 1114, 1115]
#     id_desejado = int(input('Digite o ID do produto: '))
#     if id_desejado not in produto_id:
#         raise ValueError('\nProduto não Cadastrado!')
#     else:
#         print('Produto já Cadastrado')

# except ValueError as e:
#     print(e)


# ex_3


# Dado o dicionario:

# produtos = dict(produtos=dict(p1=dict(nome="Camiseta Star Wars", preco=99.90), 
#                               p2=dict(nome='Caneca Ricky&Morty', preco=49.90), 
#                               p3=dict(nome='Camiseta SpiderMan', preco=69.90)))

# # A partir do ID do produto mostraremos o nome e o preço
# # Caso o produto não esista mostraremos a seguinte mensagem
# # Produto inexistente

# try:
#     id_produto = int(input('\nDigite o ID do produto: '))

#     if id_produto not in produtos['produtos']:
#         raise ValueError('\nProduto Inexistente!')
#     else:
# #       print(f'\nProduto: {produtos['produtos'][id_produto]['nome']}")
# #       print("\nPreco: {}".format(produtos['produtos'][id_produto]['preco'])))
#         nome = produtos['produtos'][id_produto]['nome']
#         preco = (produtos['produtos'][id_produto]['preco']
# #       print('Preço: %s' %preco)
#         print(f"Produto: {nome}")
#         print(f"Preço: {preco}")        
# except ValueError as v:
#     print(f'Erro: {v}')

# no interativo
#
# >>>produtos['produtos'].keys()
# >>>produtos['produtos']['p2'].keys()
#
## usando json para converter dict para string
#
# import json
# json.dumps(produtos)
# json.loads(produtos)
#
#
#====================================================================================================
# Manipulação de arquivos  =>  open(file 'rwxa+')
#====================================================================================================

# with open('novo_arquivo', 'w') as f:
# with open('\nnovo_arquivo', 'a') as f:
#     f.write('\nMeu primeiro arquivo')
#     f.read()
#     f.close()


# cifra.py

#!/usr/bin/python3      <shebang>

# from __future__ import print_function

# import sys

# import string    

# arquivo = open(sys.argv[1], 'r').read().lower()
# rotacao = 

# alfabeto = string.ascii_lowercase
# resultado = int(sys.argv[2])

# for letra in alfabeto:
#     if letra in alfabeto:
#         posicao = alfabeto.find(letra)
#         posicao = (posicao + rotacao) % 26
#         resultado += alfabeto[posicao]

# print(resultado)

# with open('dados_cifrados', 'w')



#====================================================================================================
# Manipulação de funções  
#====================================================================================================



# def dobra(valor):
#     return valor * 2


# print(dobra(12))


# produtos = []

# def cadastraProduto(produto):
#     return produtos.append(produto)

# ex_1

# def listaProdutos():
#     print(produtos)

# def deletaProduto(produto):
    
#     try:
#         if produto not in produtos:
#             print('Produto não cadastrado!')
#         else:
#             produtos.remove(produto)           # .remove <remove pelo objeto e .pop < remove pelo index>
#             print(f"Produto {produtos[produto]} deletado com sucesso!")
#     except valueError:

# cadastraProduto('Tenis','Sapato')

# listaProdutos(produtos)

# deletaProduto(Sapato)

#ex_2

# scopo de função global ou local

# nome = 'python'         # global

# def linux():
#     nome = 'linux'      # local
#     return nome         

# linux()
# print('\n', nome)

# nome = 'python'         # global

# def linux():
#     global nome         # mudando para global
#     nome = 'linux'      # local
#     return nome         

# linux()
# print('\n', nome)

# ex_3

# 

# ex_4

# usuarios = []



# def cadastra_Pessoa(add=None):
# # pessoa = dict(nome='Francisco', sobrenome='Cione', idade=63)
#     if add is None:
#         pass
#     else:
#         usuarios.append(add)
        
# cadastra_Pessoa('Francisco')
# cadastra_Pessoa('Cione')

# print(usuarios)




#========================================================================================================
# Manipulação de Args e Kwargs  =>  para uso de multiparametros na função qdo não se sabe qtos args terão 
#========================================================================================================



# ex_5

# frutas = []

# def insertFrutas(*args):            #  *args => *qquernome    e retorna uma tupla, que faz a vez do return
#     for f in args:                  #  descontroindo o return como tupla
#         frutas.append(f)            

# insertFrutas('abacaxi', 'banana', 'pessego', 'mamao')

# print(frutas)


# ex_6

# camisetas = {}

# def insertCamiseta(**kwargs):
#     global camisetas
#     camisetas = kwargs
#     return camisetas

# insertCamiseta(camiseta01='StarWars', camiseta02='Batman')

# print(camisetas,'\n')



#========================================================================================================
# funções Anônimas  =>  função lambda   > lambda expressão return  ( usa com => map, filter, reduce)
#========================================================================================================


# ex_7

# dobro = lambda x: x * 2

# print(dobro(10))


# Faça uma função lambda que receba 3 valores e retorne a soma

# soma = lambda x,y,z: x + y + z 

# print(soma(2, 2, 2))


# ex_8


# numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# dobro = []

# for i in numeros:
#     dobro.append(i * 2)

# fazendo por lambda map

# dobro = list(map(lambda x: x * 2, numeros))         # função map que constroi item por item
# print(dobro)


# ex_9



# fazendo por lambda filter

# dobro = list(map(lambda x: x * 2, numeros))         # função filter que constroi item por item
# numeros_par = list(filter(lambda x: x % 2 == 0, numeros))

# print(numeros_par)


# ex_9



# fazendo por lambda reduce

# from functools import reduce

# numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# dobro = list(map(lambda x: x * 2, numeros))         # função reduce que constroi item por item
# numeros_par = list(filter(lambda x: x % 2 == 0, numeros))
# soma = reduce(lambda x, y: x + y, numeros)

# print('\n<',soma,'>\n\n')

