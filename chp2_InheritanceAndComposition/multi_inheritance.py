

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


#has two base classes 
class C(A,B):
    def __init__(self):
        super().__init__()
        self.showprops()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name) #class A takes presistance because of the order; python interperter looks at the order of super classes; knon as the method resolution order 

   
c = C()

print(C.__mro__) #shows the method resolution order(mro)