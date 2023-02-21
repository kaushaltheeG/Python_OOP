

from dataclasses import dataclass 

@dataclass
class Book: 
    title: str 
    author: str 
    price: float 
    pages: int

    #allows additional properties after __init__ to be added 
    def __post_init__(self):
        self.description =  f"{self.title} by {self.author}, {self.pages}"




b1 = Book("War and Peace", "Leo Tolstoy", 39.25, 1225)
b3 = Book("War and Peace", "Leo Tolstoy", 39.25, 1225)

print(b3.description)