"""
Uma progressão aritmética (PA) é um seqüência numérica em que cada 
termo, a partir do segundo, é igual à soma do termo anterior com 
uma constante R positiva (denominada razão).

A fórmula geral de uma PA é:

an = a1 + (n - 1) . R
a(n) = a(1) + (n - 1) * R
pythonico: 
    ultimo = primeiro + (n - 1) * R

an: termo geral
a1: 1º termo
n: posição do termo geral
R: razão da P.A.

Dado um conjunto de números inteiros positivos, identificar todos 
os subconjuntos de no mínimo 3 elementos onde os números formam 
uma progressão aritmética.

Devem ser apresentados sempre os maiores subconjuntos que forme uma PA
Por exemplo, dado o subconjunto (1,2,3,5,6,7,9) teríamos como resultado:

>>> subconjunto = (1,2,3,5,6,7,9)
>>> progressao_aritmetica(subconjunto)
(1,2,3)
(5,6,7)
(1,3,5,7,9)
(3,6,9)
(1,5,9)

"""

def progressao_aritmetica(subconjunto):
    ultimo = subconjunto[-1]
    primeiro = subconjunto[0]
    # razao = subconjunto[1] - primeiro
    for i in subconjunto:
        if 
        # print(i)

# progressao_aritmetica(1, 3, 3)