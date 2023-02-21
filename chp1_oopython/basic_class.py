


#create a basic class 
# () are added to indicate that it is inheriting from another class 
class Book: 
    #function used to initial object 
    # an initializer function not a constructor becuase the object is already constructed but rather being initilzed with these fields 
    def __init__(self, title, author, pages, price):
        #self is the naming convention used for context 
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price 
        self.__secret = 'this is secrect and cannot be accessed outside of class' #unless you call it as __Book__; used to make sure subclasses don't override these attributes unless if that is what you want 

    #instance methods take in self as an argument 
    def getprice(self): 
        if hasattr(self, "_discount"):
            #checks if instances has the _discount attribute which is only avaible after setdiscount() has been called 
                return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self, amount):
        # _ indicates to other devlopers that this attribute only avaible after this methods has been run 
        self._discount = amount 


    
  

#create instances 
b1 = Book("Hi there", "k", 1225, 39.95)
b2 = Book("get me a job", "k", 1225, 39.95)


#access instance values 
print(b1.title)
print(b2.title)
print(b1.getprice())
print(b1.setdiscount(0.25))
print(b1.getprice())
