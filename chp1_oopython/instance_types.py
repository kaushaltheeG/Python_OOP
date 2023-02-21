#Important to check the instance type 
#can be achieved through type() or isinstance()

class Book: 
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name 


#instances 
b1 = Book("The K book")
b2 = Book("Python's future")
n1 = Newspaper("The New York Times")


#useful to compare two different objects 
print(type(b1))
print(type(n1))
print( type(b1) == type(n1))
print( type(b1) == type(b2))

#useful to compare an object to a know type 
print(isinstance(b1, Book))
print(isinstance(n1, Book))
print(isinstance(n1, object))

