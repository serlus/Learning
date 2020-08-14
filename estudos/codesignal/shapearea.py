"""função q de a area em relação ao valor de n
n = 1    #
          #
n = 2    ###
          #

>>> shapeArea(1)
1
>>> shapeArea(2)
5
>>> shapeArea(3)
13
>>> shapeArea(4)
25
>>> shapeArea(5)
41

"""
def shapeArea(n):
    resultado = (n ** 2) + (n  - 1)**2
    return resultado