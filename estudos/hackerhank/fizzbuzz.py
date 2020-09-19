def fizz_buzz(n):
    """A function that returns the number, in the range n
    that function returns:
    fizz for divisor 3
    buzz for divisor 5
    fizzbuzz for divisor 3 and 5
    
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
    

    """
    # Write your code here
    for i in range(n + 1):
        if i % 15 == 0: 
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

if __name__ == '__main__':
    fizz_buzz(15)