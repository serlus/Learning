def fizzBuzz(n):
    """A function that returns the number, in the range n
    that function returns:
    
    >>> FizzBuzz(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    

    Args:
        n ([type]): [description]
    """
    # Write your code here
    for i in range(n):  # for each number in n
        i += 1
        if i % 3 and i % 5 == 0:
            if i % 3 == 0:
                print('fizz')
            elif i % 5 == 0:
                print('buzz')
            print('fizzbuzz')
        else:
            print(i)


if __name__ == '__main__':
    fizzBuzz(15)