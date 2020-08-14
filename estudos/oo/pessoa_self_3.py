### Uma função q facilita a criação de nossas 'classes'
def newClass(nome, atributos):
    cls = {}  # cria um dicionário vazio para a classe
    for k, v in atributos.items():  # atribui os atributos (métodos e atributos de classe)
        cls[k] = v
    return cls 


class Pessoa(object):
    """classe pessoa ira armazenar nome e data de nascimento

    construtor, correponde ao __new__ de python
    """
    def new_pessoa(nome, nascimento):
        inst = {}  # a nova instância
        inst['classe'] = Pessoa 
        inst['nome'] = nome
        inst['nascimento'] = nascimento
        return inst

    def idade(inst, hoje):
        hd, hm, ha = hoje
        nd, nm, na = inst['nascimento']
        idade = ha - na
        return idade

    Pessoa = newClass('Pessoa', {'new_pessoa':new_pessoa, 'idade':idade})


if __name__ == "__main__":
    # ou seja para criar uma nova instancia
    hank = Pessoa['new_pessoa']('Hank Moody', (8, 11, 2007))
    Pessoa['idade'](hank, (6,11,2008))
    print(type(Pessoa))
    print(type(Pessoa.idade))