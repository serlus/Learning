# dicts

 - conecta chave a valor
 - também chamada de mapa
 - chave precisam ser 'hashable'
 - operações como as do conjunto *

 ### constant
 - [k], [k]=v, pop, in
 ### linear
 - For (no order), keys(), values(), items()

----
```python
>>> d = {'pt-BR':'Portugues Brasileiro', 'en-US':'Inglês Americano'}
>>> d['en-UK']='Inglês Britanico'
>>> d
{'pt-BR': 'Portugues Brasileiro', 'en-US': 'Inglês Americano', 'en-UK': 'Inglês Britanico'}
>>> d['en-UK']
'Inglês Britanico'
>>> d['en-UK']='Inglês Britânico'
>>> d['en-UK']
'Inglês Britânico'
>>> d
{'pt-BR': 'Portugues Brasileiro', 'en-US': 'Inglês Americano', 'en-UK': 'Inglês Britânico'}
>>> d.pop('en-US')
'Inglês Americano'
>>> for k in d: print(k)
... 
pt-BR
en-UK
>>> for k in d.values: print(k)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not iterable
>>> for k in d.values(): print(k)
... 
Portugues Brasileiro
Inglês Britânico
>>> for k in d.items(): print(k)
... 
('pt-BR', 'Portugues Brasileiro')
('en-UK', 'Inglês Britânico')
```