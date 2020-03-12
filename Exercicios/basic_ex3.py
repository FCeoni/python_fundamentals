

#========================================================================================================
# OOP - Programação Orientada a Objeto
#========================================================================================================

"""
objeto = > coisa que se abstrai do mundo real

    propriedades => caracteristicas do objeto

    métodos => comportamento ou ações que o objeto pode fazer

O programa em OOP é dividido em classes e metodos e sua principal função é a reutilização de códigos.

    Abstração =>  utilizada para definir entidades do mundo real.


    Polimorfismo => soldados tem o método atacar, mas cada classe de soldado ataca com arma diferente. 


    Encapsulamento =>  empacotar métodos 


    Herança => propriedades básicas para as quais todos os objetos possuem.


                    *****Classe não é objeto, mas sim uma abstração de sua estrutura *****







"""



#========================================================================================================
# OOP - Programação Orientada a Objeto  -  Construindo a classe carro
#========================================================================================================

# ex_1

# _*_ coding: UTF-8 _*_

# class Carro():
#     rodas = 4                   # não faz parte da construção do objeto
    
#     def __init__(self):
#         rodas = 4               # faz parte da construção do objeto


# class Carro():
    
#     def __init__(self):
#         self.rodas = 4                # faz parte da construção do objeto
#         self.porta_malas = "Normal"

#     def ligar(self):
#         print('ligado')               # este é um método

# class Fiat(carro):                    # classe carro
# carro_01 = Carro                      # instancia um único objeto da classe Carro

# class Automovel():
    
#     def __init__(self):
#         self.motor = 'combustão'

# class Carro():
    
#     def __init__(self):
#         Automovel__init__(self)
#         self.rodas = 4                  #
#         self.porta_malas = "Normal"     #
#         self.motor = True               #  Atributos
#         self.volante = True             #
#         self.tanque = True              #
    
#     def ligar(self):
#         print('ligado')             

#     def desligar(self):
#         print('carro desligado')

#     def acelerar(self):
#         print('acelerando')

#     def frear(self):
#         print('freando')

# # hilux = Carro()
# # diplomata = Carro()

# # diplomata.acelerar()

# class Fiat147(Carro):

#     def __main__(self):
# #        super().__init__()                  
# #  inicializa todos os métodos do objeto pai <o __init__ de Carro> OU
#         Carro.__init__(self)
#         self.porta_mala = 'com_agua'
#         self.motor = eletrico

# c001 = Fiat147()
# print(c001.motor)

# ex_2

# class Pai():

#     def __init__(self):
#         self.profissão = 'Advogado'

# class Mae():

#     def __init(self):
#         self.profissão = 'Médica'

# class Filho(Pai, Mae):

#     def __init__(self):
# #       Mae.__init__(self)
#         super().__init__(self)                  # dará erro por haver duas profissoes Super Classes
#         self.profissão = 'Programador'          # metodo profissao
    
#     def mudarProfissão(self, nova_profissao):
#         self.profissao = nova_profissao

#     def mudarHobby(self, nova_profissão):
#         self.mudarHobby = 'Jardineiro'


# jose = Filho()

# print(jose.profissao)                          # dará erro por haver herdado a profissao da Mae



# ex_3


# Crie uma classe Mamifero com os atributos:
#   bebe leite
#
# Crie uma classe homossapiens com atributos:
#
#   polegares = True
#   formaCaminhar = 'bipede'
#
# Métodos:
#
#   caça
#   comer
#   dormir
#   construir

# class Mamiferos():

#     def __init__(self):
#         self.bebe_leite = True
        
# class Homossapiens(Mamifero):               # ou Mamifero OU
# #    super.__init__(self):                    herança do Pai
#     def __init__(self):
#         Mamifero.__init__(self)             # Herança do Pai OU Super.__init__(self)
#         self.polegares = True               # Atributo - 1
#         self.formaCaminhar = 'bipede'       # Atributo - 2

#     def cacar(self):                        # Método - 1
#         print('caçando')

#     def comer(self):                        # Método - 2
#         print('comenndo')

#     def dormir(self):                       # Método - 3                          
#         print('dormindo')

#     def construir(self):                    # Método - 4
#         print('construindo')


# eu = homossapiens()             # instanciando

# eu.comer()                      # chamando 

# print(eu.formaCaminhar)

# print(eu.beber_leite)
    

#========================================================================================================
# OOP - Programação Orientada a Objeto  -  Módulos
#========================================================================================================

#    

# def mod1():
#     print('Mod 1')

# def mod2():
#     print('Mod 2')



# import modulefinder


# import module

# if __name__ == "__main__":          # retorna um booleano
#     mod1()
#     mod2()


 # class modd():

#     def __init__(self):
#         self.__nome = 'modulo'
#         self.__teste = 'esse é o teste'
#     def mod(self):
#         print(self.__nome)

#     def mod2(self):
#         print('Mod 2')

# m1 = modd()
# m1.mod()

for _ in range(12):
    print(1)



pip freeze 
pip freeze > requirements.txt
pip install -r requirements.txt








