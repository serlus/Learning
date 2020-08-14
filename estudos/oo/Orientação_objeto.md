# Orientação Objeto

Em orientação objeto cada objeto costuma ter uma responsabilidade, executar uma função.

class com nomecomposto deve seguir o método CamelCase
ela é como uma forma de gelo. É o molde para criar outros objetos.

```python
>>> class PessoaAlta:
        pass
```

Primeiro atributo de classe
Metodo é uma função dentro de uma classe. 
ela pertence a uma classe e esta sempre atrelada a um objeto.
também usa a palavra reservada 'def' e snakecase
Por isso deve sempre declarar o primeiro parametro a ser recebido (self)

```python
>>> class CidadãoBrasileiro:
        def cumprimentar(self):
            return 'Olá'
```

Atributo de dado ou instancia ou objeto.
eles são criados apartir do método __init__. Ele é um criador de atributos.
os atributos de dados são precedidos do primeiro parametro (self)
```python
>>> class CidadãoBrasileiro:
        def __init__(self, idade = 35):
                self.nome = None
                self.idade = idade
```

os atributos de instancia ficam presentes no atributo especial __dict__
