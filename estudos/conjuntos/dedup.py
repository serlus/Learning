def dedup(lst):
    """
    Remove duplicates from lst 
    :param lst: a list 
    : return: new list without duplicated elements

    linear for time and space
    """
    # return set(lst) a forma mais rápida seria passar a lista para um conjunto

    resultado = []
    repeated = set()

    for ele in lst:
        if ele not in repeated:
            resultado.append(ele)
            repeated.add(ele)
    return resultado

print(dedup(['banana', 'banana', 'banana', 'banana', 'abacaxi', 'caqui']))