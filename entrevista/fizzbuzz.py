def fizzBuzz(n):  # pep8
    """receber um parametro inteiro 
    q ele vai imprimir do número 1 ate o número inteiro.

    qd for divizivel por 2 fizz
    qd for divizivel por 5 buzz
    qd não for imprimir o proprio número
    casos de contorno

    >>> fizzBuzz(10)
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

    """
    n +=  1
    lista = list(range(n))  # conhecimento de range
    for i in lista[1:]:  # slice não é uma boa, 
        if i % 2 == 0 and i % 5 == 0:  # avaliar expressão boleana
            print('fizzbuzz')
        elif i % 2 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


fizzBuzz(10)