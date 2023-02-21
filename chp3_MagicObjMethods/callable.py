class Book: 
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title 
        self.author = author 
        self.price = price 


    #__str__ method is used to return a string, string representation when printing instance 
    def __str__(self):
        return f" {self.title} by {self.author} for {self.price} "

    # __call__ method can be used to call the object like funcitons 
    def __call__(self, title, author, price):
        self.title = title 
        self.author = author 
        self.price = price 
        return 




b1 = Book("War and Peace", "Leo Tolstoy", 39.25)
b2 = Book("heheh", "Leo ", 9.25)

print(b1)
b1("anna heh", "Leo", 100.0) #calling the object as a function; helps when a obj is constantly changing 
print(b1)