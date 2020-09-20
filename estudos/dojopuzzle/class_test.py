class A:
    pass

class B:
    def __init__(self, a=A()):
        self.a = a

b1 = B()
b2 = B()
a = A()

print(id(b1.a))
print(id(b2.a))
print(id(B))
print(id(A))
print(id(a))
