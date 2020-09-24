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
    total = 0
    mais = 10
    while mais != 0:
        total += mais
        while cont <= total:
            print(f'{termo} -> ', end='')
            termo += razao
            cont += 1
        print('PAUSA')
        mais = int(input('Quantos termos vc quer mostrar a mais? '))
    print('FIM')

progressao_aritimetica_2()