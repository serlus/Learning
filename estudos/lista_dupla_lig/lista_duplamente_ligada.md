# Lista duplamente ligada
# (Double Ended Queue)

<p style="color:Tomato;" >Se preciso acessar elementos apenas das pontas essa é a melhor solução</p>

1. dinamica
    - significa q posso inserir e remover elementos arbritariamente
1. funciona bem como pilha ou fila
    - fila: onde se tem o inicio em uma ponta e o fim em otra
1. Funciona bem para iteração

1. não funciona bem para acesso aleatório de elementos
    - acesso no meio da estrutura não é bom
1. Classe para essa lista
    - collections.deque
    - é preciso importar

## Análise

 | Complexidade  | Operações                               |
 | :------------:| :--------------------------------------:|
 | Constant      | Append, appendleft,pop, popleft, len    |
 | Linear        | [i], [i]=x, extend, extendleft          |


### Constant
 - **Append/pop:** inserir e remover elementos no final da fila(direita)
 - **appendleft/popleft:** inserir e remover elementos no inicio da fila(esquerda)

### Linear
 - **[i], [i]=x:** consulta um valor na lista. Será linear de acordo com a posição do elemento na lista. 
 Qt mais próximo ao centro pior o resultado.
 - **extendleft:** inserir elementos no inicio(esquerda) da lista
 - **extend:** inserir elementos no final(direita) da lista
 - **maxlen:** outra diferença é poder inserir elementos com um número max de elementos
   - circle buffer
   - quando tem esse parametro e já tem o max dele elementos:
      - se vc inserir um elemento ao inicio da lista ele remove o último
      - se vc inserir um elemento ao final da lista ele remove o primeiro

## usando
```python
>>> from collections import deque
>>> numbers = deque(range(5))
>>> numbers
deque([0, 1, 2, 3, 4])
>>> len(numbers)
5
>>> numbers.append(5)
>>> numbers
deque([0, 1, 2, 3, 4, 5])
>>> numbers.pop()
5
>>> numbers
deque([0, 1, 2, 3, 4])
>>> numbers.appendleft(-1)
>>> numbers
deque([-1, 0, 1, 2, 3, 4])
>>> numbers.popleft()
-1
>>> numbers
deque([0, 1, 2, 3, 4])
>>> numbers.extend(range(5,9))
>>> numbers
deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> numbers.extendleft(range(-1, -10))
>>> numbers
deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> numbers.extendleft(range(-10, -1))
>>> numbers
deque([-2, -3, -4, -5, -6, -7, -8, -9, -10, 0, 1, 2, 3, 4, 5, 6, 7, 8])

```