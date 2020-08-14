class Pessoa:
    Pessoa = {}
    """classe pessoa ira armazenar nome e data de nascimento

    >>> 
    construtor, correponde ao __new__ de python
    """
    def new_pessoa(nome, nascimento):
        new = {}  # a nova instância
        new['nome'] = nome
        new['nascimento'] = nascimento
        return new

    Pessoa['new'] = new_pessoa


if __name__ == "__main__":
    # ou seja para criar uma nova instancia
    hank = Pessoa['new']('Hank Moody', (8, 11, 2007))
    # print(hank['nome'])
    # print(['nascimento'])