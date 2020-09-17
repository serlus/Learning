"""
# Rotate Array
 

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. 
How many different ways do you know to solve this problem? 

>>> lista=[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> rotate_array_1(7,3)
[4, 5, 6, 7, 8, 0, 1, 2, 3]

"""
lista = list(range(9))

def rotate_array_1(n, k):
    print(lista[k])
    print(k)
    print(lista.index(n))
    print(lista[n])
    print(n)
    print(lista)

