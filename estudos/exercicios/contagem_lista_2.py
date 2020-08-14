def contar_caracteres(s):

    caracter_ordenado = sorted(s)
    caracter_anterior = caracter_ordenado[0]

    contagem = 1
    caracter = []

    for caracter in caracter_ordenado[1:]:
        if caracter == caracter_anterior:
            caracter_anterior = caracter
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    
    print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('renzo')
    print()
    contar_caracteres('banana')