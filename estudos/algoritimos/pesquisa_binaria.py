"""
Busca binaria é realizada de forma a encurtar os resultados
como tendo uma lista e usando uma busca sempre indo ao meio
e descartando a parte q não contenha a informação buscada
mas a busca binária serve apenas qd a lista esta ordenada.

"""

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = [1, 3, 5, 7, 9]
print(pesquisa_binaria(minha_lista, 3))  # => 1

print(pesquisa_binaria(minha_lista, -1))  # => None
