class Book: 
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title 
        self.author = author 
        self.price = price 
        self._discount = 0.1


    #__str__ method is used to return a string, string representation when printing instance 
    def __str__(self):
        return f" {self.title} by {self.author} for {self.price} "

    #__getattribute__ when an attr is retrieved 
    #Don't directly access the attr name otherwise a recursive loop is created 
    def __getattribute__(self, name):
        #get invoked when @book.price called 
        if name == "price":
            p = super().__getattribute__("price") #calls the parent class getatrribute to avoid recursive call 
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    # __setattr__ attribute value set function
    #Don't directly access the attr name otherwise a recursive loop is created 
    def __setattr__(self, name, value): 
        if name== "price":
            if type(value) is not float:
                raise ValueError("The pricce attr must be a floar")
        return super().__setattr__(name, value)

    # __getattr__ called when __getattribute__ fails; when the attribute does not exist 
    def __getattr__(self, name): 
        return name + " is not here"

         
    


b1 = Book("War and Peace", "Leo Tolstoy", 39.25)
b2 = Book("heheh", "Leo ", 9.25)
b3 = Book("WarPeace", "Leo Tolstoy", 39.20)
b4 = Book("War and Peace", "Leo Tolstoy", 39.0)

b1.price = 38.95 #trigger __get_ttribute__

print(b1.j)