def p_a():
    primeiro = int(input("Primeiro elemento: "))
    razao = int(input("razão: "))
    decima = primeiro + (10 - 1) * razao
    for c in range(primeiro, decima, razao):
        print(f'{c}', end=' ->')

p_a()