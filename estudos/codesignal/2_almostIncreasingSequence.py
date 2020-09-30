"""[Given a sequence of integers as an array, determine whether it
is possible to obtain a strictly increasing sequence by removing 
no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing 
if a0 < a1 < ... < an. Sequence containing only one element is also 
considered to be strictly increasing.]

>>> sequence = [1, 3, 2, 1]
>>> almostInc(sequence)
False
>>> sequence = [1, 3, 2]
>>> almostInc(sequence)
True
>>> sequence = [1, 2, 5, 3, 5]  # 1 < 2 | 2 < 5 | 5 > 3 | 3 < 5
>>> almostInc(sequence)
True
>>> sequence = [1, 2, 3, 4, 99, 5, 6]
>>> almostInc(sequence)
True
>>> sequence = [123, -17, -5, 1, 2, 3, 12, 43, 45]
>>> almostInc(sequence)
True
>>> sequence = [1,2,1,2]
>>> almostInc(sequence)
False
>>> sequence = [1, 2, 3, 4, 5, 3, 5, 6]
>>> almostInc(sequence)
False
>>> sequence = [40, 50, 60, 10, 20, 30]
>>> almostInc(sequence)
False

"""

def almostInc(sequence):
    z = len(sequence)
    z1 = len(sequence) - 1
    if sequence[0] < sequence[1]:
        n = [sequence[0]]
        before_n = sequence[0]
    elif sequence[0] > sequence[1]:
        n = [sequence[1]]
        before_n = sequence[1]
    
    f = 1
    for num in sequence[1:]:
            if before_n < num:
                n.append(num)
                before_n = num
                f += 1
            

     
    if z == f or z1 == f:
        # print('true')
        return True
    else:
        # print('false')
        return False
    


if __name__ == "__main__":


    # sequence = [1, 2, 3, 4, 99, 5, 6]
    # almostInc(sequence)
    sequence = [123, -17, -5, 1, 2, 3, 12, 43, 45]
    almostInc(sequence)
    # sequence = [1,2,1,2]
    # almostInc(sequence)
    sequence = [1, 2, 3, 4, 5, 3, 5, 6]
    almostInc(sequence)
    # sequence = [40, 50, 60, 10, 20, 30]
    # almostInc(sequence)
    # sequence = [1, 3, 2, 1]
    # almostInc(sequence)
    sequence = [1, 3, 2]
    almostInc(sequence)
    # sequence = [1, 2, 3, 4, 5]
    # almostInc(sequence)
    # sequence = [1, 3, 5]
    # almostInc(sequence)
    sequence = [1, 2, 5, 3, 5]
    almostInc(sequence)

    