#__str__ and __repr__ are helpful for debugging by showing attributes more clearly 
#

class Book: 
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title 
        self.author = author 
        self.price = price 


    #__str__ method is used to return a string, string representation when printing instance 
    def __str__(self):
        return f" {self.title} by {self.author} for {self.price} "
    #__repr__ used to return an obj representation; debugging purposes
    def __repr__(self):
        return f"title={self.title} author={self.author} price={self.price}"



b1 = Book("War and Peace", "Leo Tolstoy", 39.25)
b2 = Book("heheh", "Leo ", 9.25)


print(b1)
print(b2)

#Before __str__
#<__main__.Book object at 0x1026e89d0>
#<__main__.Book object at 0x1026e8a10>

#with __str__
#  War and Peace by Leo Tolstoy for 39.25 
#  heheh by Leo  for 9.25 

print(str(b1))
print(repr(b2))

# War and Peace by Leo Tolstoy for 39.25 
#title=heheh author=Leo  price=9.25
