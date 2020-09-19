def hanoi(n, orig='A', aux='B', dest='C'):
    """[summary]

    Args:
        n ([type]): [description]
        orig (str, optional): [description]. Defaults to 'A'.
        aux (str, optional): [description]. Defaults to 'B'.
        dest (str, optional): [description]. Defaults to 'C'.
    """
    if n >= 1:
        hanoi(n - 1, orig, dest, aux)
        # print('{} -> {} : {}'.format(orig, dest, n))
        print(f'{orig} -> {dest} : {n}')
        hanoi(n - 1, aux, orig, dest)

for i in range(1, 4):
    print('###### Hanoi %s' % i)
    hanoi(i)