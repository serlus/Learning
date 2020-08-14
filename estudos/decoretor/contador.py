def fabrica_de_contador():
    contador = 0

    def contar():
        nonlocal contador  # assim consigo acessar uma variavel fora desse escopo
        # global faz a mesma função de acessar objetos fora do escopo, mas globais
        contador += 1  # esse contador é diferente do definido fora dessa função
        return contador
    
    return contar


contador = fabrica_de_contador()
contador_2 = fabrica_de_contador()
print(contador())
print(contador())
print(contador())
print(contador_2())
print(contador_2())
