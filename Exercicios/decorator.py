# ==============================================================================================
# decorator  -  primeiro exemplo
# ==============================================================================================

# import time


# def calcula_duração (função):

#     def wrapper():
#             tempo_inicial = time.time()
#             função()
#             tempo_final = time.time()

#         print(f"[{funcao.__name__}] Tempo total de execução: {tempo_final - tempo_inicial}")

#     return wrapper


# @calcula_duracao
# def main():
#     for i in range(0, 1000000000):
#         pass

# main()


# ==============================================================================================
# decorator  -  segundo exemplo
# ==============================================================================================



usuarios = dict(renato='abacaxi123', carlos='fusca123', maria='teste321')
bloqueados = []
tentativas = 0

import time


def calcula_duracao(funcao):

    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        print(f"[{funcao.__name__}] Tempo total de execução: {tempo_final - tempo_inicial}")

    return wrapper


@calcula_duracao
def login():
    while True:
        login = input('Digite o seu usuario: ')
        if login in usuarios:
            senha = input('Digite sua senha: ')
            if senha == usuarios[login]:
                print('login efetuado!')
                break
            elif tentativas < 3:
                print('Senha Incorreta!')
                tentativas += 1
                continue
            else:
                print('Usuário bloqueado, contate o administrador')
                bloqueados.append(login)
                usuarios.pop(login)
                break
        else:
            print('Usuário não cadastrado')
            continue

login()

# print(f'usuarios: {usuarios}')
# print(f'usuarios bloqueados: {bloqueados}')


# frutas = ['uva', 'banana', 'laranja']


# for i,f in enumerate(frutas):
#     print(i, f)



