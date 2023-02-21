#when to use class-level and static methods 

class Book:
    #CLASS ATRRIBUTE: properties defined at the cless level are shared by all instances 
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", 'EBOOK')
    #double-underscore properties are hidden from other classes; private variable 
    __booklist = None

    #class method: returns the book type constant 
    @classmethod
    def getbooktypes(cls):
        #cls refers to this class 
        return cls.BOOK_TYPES

    #static method: they dont modify the state of that instance or class; useful when not needing to access properties of a particular object or namespaceing certain methods 
        #taking a global function/variable or var and putting it into the class's namespace 
        #great when implementing a signleton desgin pattern: one one instance of an object is created 
    @staticmethod
    def getbooklist():
        #only one is created 
        if (Book.__booklist == None):
                Book.__booklist = []
        return Book.__booklist 


    #instance method 
    def setTitle(self, newtitle): 
        self.title = newtitle

    #initializing method 
    def __init__(self,title, booktype) -> None:
        self.title = title 

        if (not booktype in Book.BOOK_TYPES): raise ValueError(f"{booktype} is not in valid book types")
        else: self.booktype = booktype

print(Book.getbooktypes())
b1 = Book("The K book", "HARDCOVER")
b2 = Book("Python's future", 'HARDCOVER')

#the static methos the access a signleton object 
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
