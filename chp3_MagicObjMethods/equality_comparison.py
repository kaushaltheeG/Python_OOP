class Book: 
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title 
        self.author = author 
        self.price = price 


    #__eq__:  to check of two objs attributes are equal 
    def __eq__(self, other): # added == to Book class by over riding it 
        if not isinstance(other, Book): raise ValueError("Cannot compare a non-book instance") 
        return (self.title == other.title) and (self.author == other.author) and (self.price == other.price)
    #__ge__ est >= relationship with another obj 
    def __ge__(self, other):
        if not isinstance(other, Book): raise ValueError("Cannot compare a non-book instance") 

        return self.price >= other.price
    # __lt__ est < relationship with another obj 
    def __lt__(self, other): 
        if not isinstance(other, Book): raise ValueError("Cannot compare a non-book instance") 
        return self.price < other.price
         
    


b1 = Book("War and Peace", "Leo Tolstoy", 39.25)
b2 = Book("heheh", "Leo ", 9.25)
b3 = Book("WarPeace", "Leo Tolstoy", 39.20)
b4 = Book("War and Peace", "Leo Tolstoy", 39.25)





print(b1 == b4)
print(b1 >= b3)
print(b2 < b3)

#now we can sort them because built in sort uses these comparison operators which are overwritten 
books = [b1, b2, b3, b4]
books.sort()
print(books)

