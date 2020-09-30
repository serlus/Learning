# Conjuntos

Operações em conjuntos
não possui elementos repetidos
    ele verifica se o elemento inserido já exite no conjunto por isso não repete
Hash
numeros, string, tupla -> imutáveis
estrutura boa para fazer backtrack

**constant**
 - add
 - remove
 - in

**Linear**
 - for (no order)
 - union
 - '-'
 - intersection

 built-in

---- 

## usando
### Constant
```python
>>> s=set()
>>> s.add(1)
>>> s
{1}
>>> s.add(2)
>>> s
{1, 2}
>>> s.remove(2)
>>> s
{1}
>>> 2 in s
False
>>> 1 in s
True
>>> s2=set(range(10))
>>> s2
```
### Linear
```python
>>> s2.union(s)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s.add(40)
>>> s.add(50)
>>> s2
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s2.union(s)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 40, 50}
>>> s2
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s
{40, 1, 50}
>>> s2-s
{0, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s2.intersection(s)
{1}
>>> for e in s2:
...     print(e)
... 
0
1
2
3
4
5
6
7
8
9

```