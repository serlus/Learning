from random import shuffle

def max_min(lst):
    """
    Calculate the maximum and minimum of a list lst
    :param: lst: list 
    :return: tuple: (max, min)

    """
    if len(lst) == 0:  # contains
        raise ValueError('Empty List')
    # return lst[-1], lst[0]  # 0(1) 
    # return max(lst), min(lst)  # 0(n + n)
    max_value = min_value = lst[0]

    for value in lst:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value
    return max_value, min_value  # 0(n)

print(max_min([1]))  # 1,1
print(max_min([1,2]))  # 2,1
random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_min(random_list))  # 99, 0
print(max_min([]))  # ValueError: Empty list