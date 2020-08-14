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
    n = len(lst)
    if n == 0:  # lst (const)
        raise ValueError('Empty List')
    max_value = min_value = lst[-1]  # uso mais memoria constante, mas apenas uma vez
    
    def max_min_rec(cursor):
        if cursor < 0:
            return max_value
    return max_min_rec(n-1)
    

print(max_min([1]))  # 1,1
print(max_min([1, 2]))  # 1, 2
print(max_min(list(range(100))))  # 0, 99
random_list = list(range(100))
shuffle(random_list)
print(max_min(random_list))
print(max_min([]))  # error