class A:
    pass

class B:
    def __init__(self, a=None):
        if not a:
            self.a = A()
        else:
            self.a = a

b1 = B()
b2 = B()

print(id(b1.a))
print(id(b2.a))
