### Uma função q facilita a criação de nossas 'classes'
def newClass(nome, atributos):
    cls = {}  # cria um dicionário vazio para a classe
    for k, v in atributos.items():  # atribui os atributos (métodos e atributos de classe)
        cls[k] = v
    return cls 


class Pessoa:
    """classe pessoa ira armazenar nome e data de nascimento

    construtor, correponde ao __new__ de python
    """
    def new_pessoa(nome, nascimento):
        inst = {}  # a nova instância
        inst['nome'] = nome
        inst['nascimento'] = nascimento
        return inst

    Pessoa = newClass('Pessoa', {'new_pessoa':new_pessoa})


if __name__ == "__main__":
    # ou seja para criar uma nova instancia
    hank = Pessoa['new']('Hank Moody', (8, 11, 2007))
