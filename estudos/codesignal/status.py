"""função q busque em uma lista de estatuas a q falta
para manter uma ordem desde a menor até a maior

>>> statues = [6, 2, 3, 8]
>>> makeArray(statues)
3
>>> statues = [0, 3]
>>> makeArray(statues)
2
>>> statues = [5, 4, 6]
>>> makeArray(statues)
0

"""
def makeArray(statues):
    maior = max(statues)
    menor = min(statues)
    
    lista_previa = list(range(menor, maior+1))
    return len(lista_previa) - len(statues)