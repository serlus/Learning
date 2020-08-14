def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex.: 
    >>> contar_caracteres('renzo')
    {'e':1, 'n':1, 'o':1, 'r':1, 'z':1}
    >>> contar_caracteres('banana')
    {'a':3, 'b':1, 'n':2}

    :param s: string a ser contada
    """
    resultado = {}  # colocar o resultado em um dicionario vazio
 # solução 1
    # for caracter in s:
        # contagem = resultado.get(caracter, 0)
        # contagem += 1
        # resultado[caracter]=contagem
 # solução 2
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado  # precisa retornar


if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print()
    print(contar_caracteres('banana'))
