#Data classes help remove boiler plate code 
from dataclasses import dataclass 

@dataclass
#will rewrites the __init__function and attributes have defined data types; they are not enforced tho
class Book: 
    title: str 
    author: str 
    price: float 
    pages: int

    def bookinfo(self):
        return f"{self.title}, ${self.author}"
#heh



b1 = Book("War and Peace", "Leo Tolstoy", 39.25, 1225)
b3 = Book("War and Peace", "Leo Tolstoy", 39.25, 1225)

b2 = Book("heheh", "Leo ", 9.25, 300)

print(b1.author)
print(b2.author)

#the == now works; does not compare memory od 
print(b1 == b3)

b2.author = 'k'
print(b2)