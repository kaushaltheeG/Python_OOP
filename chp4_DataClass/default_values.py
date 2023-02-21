from dataclasses import dataclass, field 
#field is another way for adding default values 
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book: 
    title: str = "No title"
    author: str = "No Author"
    price: float = field(default_factory=price_func)  
    pages: int =  field(default=0)



b1 = Book()
print(b1)




