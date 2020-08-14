"""
fonte: http://dojopuzzles.com/problemas/exibe/ocr-bancario/
Você trabalha para um banco, que recentemente comprou uma máquina muito
engenhosa para auxiliar na leitura de cartas e faxes enviados para o
escritório-central. Esta máquina escaneia os documentos em papel e produz
um arquivo com um grande número de entradas, sendo que cada uma tem este formato:

     _  _       _   _  _   _   _
  |  _| _| |_| |_  |_   | |_| |_|
  | |_  _|   |  _| |_|  | |_|  _|

Cada entrada possui 4 linhas, e cada linha possui 27 caracteres. 
As 3 primeiras linhas contém o número da conta, utilizando pipes e underscores, 
e a quarta linha é vazia. 
Cada número de conta possui nove dígitos (entre 0 e 9). 
Cada arquivo pode conter até 500 registros. 

Sua tarefa é desenvolver um programa que obtenha esse
arquivo e devolva a lista de contas.

1) gerar um programa q gera arquivos.
2) cada arquivo pode conter 500 registro
3) cada registro é formado por 9 digitos
4) é formado por 4 linhas 
    1
1ª      _   _
2ª   |  _|  _|
3ª   | |_   _|
4ª

>>> n(1)
     _  _       _   _  _   _   _
  |  _| _| |_| |_  |_   | |_| |_|
  | |_  _|   |  _| |_|  | |_|  _|

 
>>> n(2)
 _
 _|
|_


>>> n(3)
 _
 _|
 _|

>>>

"""

def n(s):
  pass
#   lista = list(range(10))
#   for _ in lista:
#     if _ == 1 or 4:
#       print()
#       print('  |')
#       print('  |')
#       print()
#   elif s == 2:
#     print(' _')
#     print(' _|')
#     print('|_')
#     print('')

# if __name__ == '__main__':
#   n(1)
