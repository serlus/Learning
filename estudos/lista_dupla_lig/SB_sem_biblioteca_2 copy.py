from collections import deque


def less_to_great_significant_digit(s):
    result = []
    s = list(s)
    while s:
        result.append(int(s.pop()))
    return result

def zip_longest(n, n2, fillvalue):
    n = list(n)
    n2 = list(n2)
    minor, greater = sorted([n, n2], key=len)
    missing = len(greater) - len(minor)
    minor.extend([fillvalue] * missing)
    result = []
    for i, d in enumerate(greater):
        result.append((d, minor[i]))
    return result

def binary_sum(n, n2):
    """
    n and n2 are non negative binary numbers with arbitrary len.
    Ex: '00010101001010101010101010101010101001010101010101010'
    
    linear: O(max(n, n2)) 
    
    o número relacionado a string tem relação com a memória

    agora usando a lib disponivens em python
    """
    n = less_to_great_significant_digit(n)
    n2 = less_to_great_significant_digit(n2)
    last_d_sum = 0
    result = deque()
    for d, d2 in zip_longest(n, n2, fillvalue=0):
        d_sum = last_d_sum + d + d2
        last_d_sum = 0 if d_sum < 2 else 1
        result.appendleft(str(d_sum % 2))
    if last_d_sum == 1:
        result.appendleft('1')

    return ''.join(result)





print(binary_sum('10101011', '1000'))