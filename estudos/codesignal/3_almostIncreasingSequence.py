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
    z = len(sequence)
    f = 1
    before_n = sequence[0]
    # n = []
    for num in sequence[1:]:
        if before_n < num:  # 1 < 3 | 3 < 2 | 
            # n = before_n
            f += 1
            before_n = num
        elif before_n >= num:
            before_n = num
    # f = len(n)
    if z == f or z - 1 == f:
        print('true')
    else:
        print('false')

if __name__ == "__main__":
    sequence = [1, 3, 2, 1]
    almostInc(sequence)
    sequence = [1, 2, 3]
    almostInc(sequence)
    sequence = [1, 2, 5, 3, 5]  # 1 < 2 | 2 < 5 | 5 > 3 | 3 < 5
    almostInc(sequence)
    sequence = [1, 2, 3, 4, 99, 5, 6]
    almostInc(sequence)
    sequence = [123, -17, -5, 1, 2, 3, 12, 43, 45]
    almostInc(sequence)
    

