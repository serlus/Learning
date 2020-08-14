import collections


Carta = collections.namedtuple('Carta', ['valor', 'naipe'])
"""
namedtuple é uma meta class q cria class 
nome da class [atributos da class]

"""

class Baralho:
    valores = (str(n) for n in range(2,11)) + list('JOKA')
    naipes = 'paus ouros copas espadas'.split()
    def __init__(self):
        self.cartas = (Carta(v, s) for n in self.naipes for v in self.valores)
        """list compreetion, cria um produto cartesiano com lista de pares e valores possiveis"""
    def __len__(self):
        return len(self.cartas)
        """para q os operadores da class respondam ao len"""
    def __getitem__(self, posicao):
        return self.cartas(posicao)
        """para funcionar como coleção, assim os item sendo acessados como dicionario
            atraves de colchetes
        """