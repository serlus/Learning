from itertools import permutations

"""
 Este problema foi utilizado em 430 Dojo(s).

Escreva um programa que gere todos os anagramas potenciais de uma string.

Por exmplo, os anagramas potenciais de "biro" são:

biro bior brio broi boir bori
ibro ibor irbo irob iobr iorb
rbio rboi ribo riob roib robi
obir obri oibr oirb orbi orib

"""
def anagrama(s):
    palavra = [char for char in s]
    n = len(palavra)
    resultado = [''.join(x) for x in permutations(palavra, n)]
    print(resultado)


if __name__ == '__main__':
    anagrama('tree')