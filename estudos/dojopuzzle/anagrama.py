import random

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
    resultados = [s]
    palavra_anterior = resultados[0:]
    # possibilidade_b = s[0:]
    palavra = ''.join(random.sample(s, len(s)))
    # print(palavra_anterior)

    for palavra_anterior in resultados:
        if palavra != palavra_anterior:
            resultados.append(palavra)
            palavra_anterior = palavra
            palavra = ''.join(random.sample(s, len(s)))
            # print(palavra_anterior)
        else:
            palavra == palavra_anterior
    return resultados
    
    # print(resultados)
    # print(palavra)
    # print(resultados)
    # return resultados

if __name__ == '__main__':
    print(anagrama('biro'))