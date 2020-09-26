def fizzbuzz(n):
    """
    docstring
    """
    for i in range(1, n + 1):
        resultado = ''

        if i % 2 == 0:
            resultado = 'fizz'
        elif i % 3 == 0:
            resultado = 'buzz'
        
        print(resultado if resultado != '' else i)

fizzbuzz(10)