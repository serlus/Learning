def binary_sum(n, n2):
    """
    n and n2 are non negative binary numbers with arbitrary len.
    Ex: '00010101001010101010101010101010101001010101010101010'
    o número relacionado a string tem relação com a memória

      1100
    111110
    0+0 = 0
    0+1 = 1
    1+1 = 2 / 2 = 0           (1 para a próxima soma)
    1+1 = 2 + 1 = 3 / 2 = 1  (1 para a próxima soma)
      1 = 1 + 1 = 2 / 2 = 0  (1 para a próxima soma)
      1 = 1 + 1 = 2 / 2 = 0  (1 para a próxima soma)
      1 = 1

    0 + 0 = 0
    1 + 1 =         2 / 2 = 0  (1 para a próxima soma)
    0 + 1 = 1 + 1 = 2 / 2 = 0 (1 para a próxima som)
    1 + 0 = 1 + 1 = 2 / 2 = 0 (1 para a próxima)
        0 = 0 + 1 = 1
        1 = 1

    Aproveitando as funcinalidades de python q permite int de tamanhos arbitrário, 
    podemos resolver da seguinte forma.
    int tem um segundo parametro q é a base
    com format posso tornar em string novament um int e 'b' indicando binario
    """
     
print(binary_sum('10101011', '1000'))