def contar_caracteres(word):
    """receber uma palavra e contar caracteres recursivos

    Args:
        word ([str]): [qualquer palavra]
    exemplo:
    >>> contar_caracteres('banana')
    {'b': 1, 'a': 3, 'n': 2}
    >>> contar_caracteres('sergio')
    {'s': 1, 'e': 1, 'r': 1, 'g': 1, 'i': 1, 'o': 1}

    """
    resultado = {}

    for letter in word:
        resultado[letter] = resultado.get(letter, 0) + 1

    return resultado

print(contar_caracteres('paralelepipido'))