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
    f = 0
    n = []
    for a, b in zip(sequence, sequence[1:]):
        if a < b:
            n = a
            # f += 1
        elif a >= b:
            pass
    if z == f or f-1:
        print('true')
    else:
        print('false')

if __name__ == "__main__":
    sequence = [1, 3, 2, 1]
    almostInc(sequence)
    sequence = [1, 2, 3]
    almostInc(sequence)
    

