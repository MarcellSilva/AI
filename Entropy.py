# Criando uma função que recebe a quantidade (em inteiros) de dois elementos 'na' e 'nb' e retornando o valor da entropia do conjunto.
# Utilizei o math.log2(p) para calcular o valor do log base de uma probabilidade.
# Printando alguns valores como teste do código.

import math


def entropia(na, nb):
    entropia = 1
    ### Seu código começa aqui ###

    s1 = na / (na + nb)
    s2 = nb / (na + nb)
    s0 = s1 + s2

    if na <= 1 or nb <= 1:
        return 0
    else:
        entropia = abs((s1*math.log2(s1)) + (s2*math.log2(s2)))

    ### Seu código termina aqui ###
    return entropia


if __name__ == '__main__':
    print(entropia(50, 50))
    print(entropia(10, 50))
    print(entropia(10, 100))
    print(entropia(0, 100))
    print(entropia(10, 0))
