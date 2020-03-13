# Dado a Lista:

# times = [['Corinthias', 'Palmeiras', 'São Paulo'], ['Preto', 'Branco', 'Verde', 'Vermelho']]

# # imprima na tela as seguintes mensagens:
# #time: <nome_time>, cores: <cores_time>

# print('Time: ',times[0][0], 'Cor: ',times[1][0], times[1][1])
# print('Time: ',times[0][1], 'Cor: ',times[1][3])
# print('Time: ',times[0][2], 'Cor: ',times[1][0], times[1][1], times[1][3])

# print(f'Time: {times[0][0]} Cor: {times[1][0]} {times[1][1]}')


print('\n\n\n')

# for i in times[0]:
#     for n in times[1]:
#         if times [0]
#         print(f'time: {i}') 

# Dado a Tupla:

# linguagens = ('python', 'java', 'goland')

# print('\n\n\n')
# Dado o Dicionario:
# dicionário(chave:valor)

# carros = {'modelos':{'Fox','Fusca', 'Palio'}, 
#             'anos':{1223, 1978, 2002}}

# print(carros['modelos'])
# print(carros['anos'])

# print('\n\n\n')

# produtos = {'produtos': {'001': {'nome': 'Camiseta SpiderMan',
#                                     'preço': 99.90},
#                         '002':  {'nome': 'Camiseta Star Wars',
#                                     'preço': 79.90}
#                         }
#             }

# print(produtos.keys())
# print('\n')
# print(produtos['produtos']['002']['preço'])
# print('\n')
# print(produtos['produtos']['001']['preço'])
# print('\n')
# print(produtos['produtos']['001']['nome'])
# print('\n')
# print(produtos['produtos']['002']['nome'])
# print('\n')

# produtos['produtos']['001']['preço'] = int(29.90)

# print(produtos)

# print(produtos['produtos']['001'].values())

# dado o dicionario:

dados = {
    'estados': {
    'sp' :{
        'nome': 'São Paulo',
        'municipios': 645,
        'população': 44.04
    },
    'rj'  :{
        'nome': 'Rio de Janeiro',
        'municipios': 92,
        'população': 16.72
    },
    'mg'  :{
        'nome': 'Minas Gerais',
        'municipios': 31,
        'população': 20.87
    }
}
}

# Imprima na tela as seguintes mensagens:

# Estado: <nome_estado>
# Municipios: <qtde_municipios>
# População: <qtde_população>

print(f"Estado: {dados['estados']['sp']['nome']}\nMunicipios: {dados['estados']['sp']['municipios']}\nPopulação: {dados[estados]['sp']['população']}")

# print(f"Estado: {}\nMunicipios: {}\nPopulação: {}", dados[0][1][1], dados[0][1][2], dados[0][1][3])

print('\n')

for estado in dados['estados'].key():
    print(f"Estado: {dados['estados'][estado]['nome]']}")
    print(f"Municipios: {dados['estados'][estado]['municipios']}")
    print(f"População: {dados['estados'][estado]['população']}")
    print(' ')