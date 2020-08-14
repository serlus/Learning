
class Pessoa(object):
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    
    def idade(self, hoje):
        hd, hm, ha = hoje
        nd, nm, na = self.nascimento
        x = ha - na
        return x


if __name__ == "__main__":
    fante = Pessoa('John Fante', (8, 4, 1909))
    print(fante.idade((6, 11, 2008)))
    print(fante['nome'])
