class Pessoa:
    olhos = 2  # atributo de class ou default
    mamifero = True
    bípede = True
    def falar(self):
        pass


class CidadaoBrasileiro(Pessoa):
    def __init__(self, *filhos, nome = None, idade = None):  # método especial de criação de atributos
        self.nome = nome  # 'self.nome' = atributo de dado; nome = parametro do método
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá sou {self.nome}'

    def beber(self):
        return 'café'


class Mineiro(CidadaoBrasileiro):
    def cumprimentar(self):
        return 'Taaarde'
        
    def beber(self):
        return 'café com pão de queijo'


if __name__ == '__main__':
    sergio = CidadaoBrasileiro(nome='Sergio')
    lucimar = CidadaoBrasileiro(sergio, nome='Lucimar')
    print(lucimar.cumprimentar())
    print(CidadaoBrasileiro.cumprimentar(sergio))
    for filho in lucimar.filhos:
        print('o filho ', filho.nome)
    p = Mineiro(nome='Firmino')
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Sergio'
    print(p.nome)
    print(p.beber())
    print(sergio.__dict__)
    print(lucimar.__dict__)


