"""
faça um programa q leia um numero inteiro
e retorne se ele é primo ou não.
número primo só é divisível por 1 e por ele mesmo
"""
def calcular_numero_primo():
    num = int(input('Digite um numermo: '))
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[34m', end='')
            tot += 1
        else:
            print('\033[31m', end='')
        print(f' {c} ', end='')

    print(f'\n\033[m O número {num} foi divisível {tot} vezes.')
    if tot == 2:
        print('É primo!')
    else:
        print('Não é primo!')

calcular_numero_primo()