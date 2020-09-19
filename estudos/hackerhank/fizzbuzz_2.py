def fizz_buzz(n):
    """
    passado um parametro inteiro n onde deve retornar
    fizz se for divisível por 2
    buzz se for divisível por 5
    e o próprio número se for divisível pelo dois

    >>> fizz_buzz(10)
    1
    fizz
    3
    fizz
    buzz
    fizz
    7
    fizz
    9
    fizzbuzz

    terminei em 9 min 
    18/09/2020
    """

    for i in range(n):
        i += 1
        if i % 2 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 2 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

fizz_buzz(30)