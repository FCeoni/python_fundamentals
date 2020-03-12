import os

os.system('clear')

#Programa Folha de Pagamento

"""
objeto empregado
metodos salario, horas, sal_bruto, desc_ir, desc_sind, cont_fgts
"""

#!/usr/bin/python3

salario = float(input("Digite o valor hora: "))

horas_trab = float(input("Digite as horas tranalhadas: "))

salario_bruto = (salario * horas_trab)

if salario_bruto >= 4600:
    irpf = 27
elif salario_bruto > 3700 and salario_bruto <= 4600:
    irpf = 22
elif salario_bruto > 2800 and salario_bruto <= 3700:
    irpf = 15
elif salario_bruto > 1900 and salario_bruto <= 2800:
    irpf = 7
else:
    irpf = 0

valorIR = salario_bruto * (irpf / 100.0)
valorSindicato = salario_bruto * (3/100.0)
valorContribuição = salario_bruto * (11/100.0)

totalDescontos = valorIR + valorSindicato

salario_liquido = salario_bruto - totalDescontos

print(f"Valor da hora: {salario}")
print(f"Quantidade de horas trabalhadas: {horas_trab}")
print(f"Salario bruto: {salario_bruto}")
print(f"(-) IR ({irpf}%): R${valorIR}")
print(f"(-) Sindicato (3%) R$ {valorSindicato}")
print(f"FGTS (11%): {valorContribuição}")
print(f"Total de descontos: R$ {totalDescontos}")
print(f"Salario Líquido: R$ {salario_liquido}")

# empregado = {'salario': 'valor', 'horas':'acumulada', 'desc_ir':'faixa', 'desc_sind':'valor', 'cont_fgts':'valor'}

# print(empregado)

