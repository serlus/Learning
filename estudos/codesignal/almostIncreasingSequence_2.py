"""[Given a sequence of integers as an array, determine whether it
is possible to obtain a strictly increasing sequence by removing 
no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing 
if a0 < a1 < ... < an. Sequence containing only one element is also 
considered to be strictly increasing.]

>>> sequence = [1, 3, 2, 1]
>>> almostInc(sequence)
false
>>> sequence = [1, 3, 2]
>>> almostInc(sequence)
true
"""

def almostInc(sequence):
    z = len(sequence) -1
    # n = []
    f = 0
    n = [a for a, b in zip(sequence, sequence[1:]) if a < b in sequence]
    print(n)
            # pop()
            # n = True
            # f += 1
        # elif a >= b:  # como fazer o elemento 'b' passar a ter o valor do prox elemento?
    # print(n)
    
    if z == f or f-1:
        print('true')
        return True
    else:
        print('false')
        return False
    


if __name__ == "__main__":
    sequence = [1, 3, 2, 1]
    almostInc(sequence)
    sequence = [1, 3, 2]
    almostInc(sequence)
    sequence = [1, 2, 3, 4, 5]
    almostInc(sequence)
    sequence = [1, 3, 5]
    almostInc(sequence)
    