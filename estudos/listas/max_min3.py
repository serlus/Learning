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
    max_value = min_value = lst[0]  # uso mais memoria constante, mas apenas uma vez

    for value in lst:  # iterar pelos valores presentes em lst. apenas um for
        if value > max_value:
            max_value = value  # atualiza valor para max
        if value < min_value:
            min_value = value  # atualiza valor para min
            """
            diferente de usar a lib min e max com essa formula estou usando uma complexidade
            maior para implementar mas um valor menor de memoria de execução.
            """
    return max_value, min_value
    

print(max_min([1]))  # 1,1
print(max_min([1, 2]))  # 1, 2
print(max_min(list(range(100))))  # 0, 99
random_list = list(range(100))
shuffle(random_list)
print(max_min(random_list))
print(max_min([]))  # error