from random import shuffle


def max_min(lst):
    """
    Função que me retorana min e max de uma lista
    calcular o valor max e min da lista
    Calculate the maximum and minimum of a list lst
    falar tb do tempo de execução se constante, linear...
    :param lst: list
    :return: tuple:(max, min)
    """
    if len(lst)  == 0:  # lst (const)
        raise ValueError('Empty List')  
    return lst[-1], lst[0]  # 0(1)(const)
    

print(max_min([1]))  # 1,1
print(max_min([1, 2]))  # 1, 2
print(max_min(list(range(100))))  # 0, 99
random_list = list(range(100))
shuffle(random_list)
print(max_min(random_list))
print(max_min([]))  # error