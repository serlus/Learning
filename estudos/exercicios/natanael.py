def contar_caracteres(s):
    ordenacao_dos_caracteres = s
    caracter = ordenacao_dos_caracteres[0]
    contagem = 1
    letra={}
    for c in ordenacao_dos_caracteres[1:]:
        if c == caracter:
            contagem += 1
        
        else:
            letra={{caracter}: {contagem}}
            caracter = c
            contagem = 1
    return letra={{caracter}: {contagem}}

if __name__=='__main__':
    print(contar_caracteres('natanael'))
    print()
