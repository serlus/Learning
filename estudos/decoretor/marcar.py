from estudos.decoretor.registrador import get_marcadas, marcar

def primeira():
    pass

primeira = marcar(primeira)  # é uma design pattern

@marcar  # realiza a mesma expressão assim de retornar a mesma função
def segunda():
    pass

if __name__ == '__main__':
    for f in get_marcadas():
        print(f.__name__)
