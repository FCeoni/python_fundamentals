
# cifra.py

#!/usr/

from __future__ import print_function

import sys

import string    

arquivo = open(sys.argv[1], 'r').read().lower()
rotacao = 

alfabeto = string.ascii_lowercase
resultado = int(sys.argv[2])

for letra in alfabeto:
    if letra in alfabeto:
        posicao = arquivo.find(letra)
        posicao = (posicao + rotacao) % 26
        resultado += alfabeto[posicao]

print(resultado)

with open('dados_cifrados', 'w')
    d.write(resultados)
