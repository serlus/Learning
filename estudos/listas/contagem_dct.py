"""

>>> contar_caracteres('sergio')
{s: 1, e: 1, r: 1, g: 1, i: 1, o: 1}
>>> contar_caracteres('banana')
{b: 1, a: 3, n: 2}
"""
def contar_caracteres(nome):
    """contagem de caracteres passados e armazenar em um dicionário
    
    Args:
        nome ([str]): [string em geral nome]

    Returns:
        [dct]: [retorna uma contagem dentro de um dicionário com a contagem de cada
        caractér]

    para isso foi utilizado um dicionário vazio para armazenar
    a função get: ira buscar o elemento dentro do dicionário se ele não estiver la
    ira adicionar o valor 0 e acrescentar o valor 1 ao resultado e ira novamente armazenar
    ele no dicionário(resultado)
    """
    resultado = {}

    for caracter in nome:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('sergio'))
    print()
    print(contar_caracteres('sergio luis morais casas'))
    print()
    print(contar_caracteres('rafaela piva casas'))