"""
calcular progressão aritmética com laço while
mostrando os dez primeiros termos
"""
def progressao_aritimetica_2():
    print('Gerador de PA')
    print('-=' * 10)
    primeiro = int(input('primeiro termo: '))
    razao = int(input('razao da PA: '))
    termo = primeiro
    cont = 1
    while cont <= 10:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1

progressao_aritimetica_2()