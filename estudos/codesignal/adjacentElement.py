def adjacent(inputlista):
    """uma função que multiplique os elementos de uma lista
    apenas com seus pares adjacentes
    verificar qual maior resultado
    retornar o resultado maior

    Args:
        parameter_list ([type]): [description]
    
    >>> lista1 = [1, 5, 3, 4, 6]
    >>> adjacent(lista1)
    24
    >>> lista2 = [3, 5, 2]
    >>> adjacent(lista2)
    15

    """
    prelista = [v * b for v, b in zip(inputlista, inputlista[1:])]
    prelista.sort()
    print(prelista[-1])

if __name__ == "__main__":
    lista = [1, 5, 3, 4, 6]
    adjacent(lista)