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
    l = []
    for i in sequence:
        if i not in sequence:
            l.append(i)
    l.sort()

    if l == sequence or z - 1 == f:
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
    

