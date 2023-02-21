


#create a basic class 
# () are added to indicate that it is inheriting from another class 
class Book: 
    #function used to initial object 
    # an initializer function not a constructor becuase the object is already constructed but rather being initilzed with these fields 
    def __init__(self, title):
        #self the the naming convention used for context 
        self.title = title
        
    
  

#create instances 
b1 = Book("Hi there")
b2 = Book("get me a job")


#access instance values 
print(b1.title)
print(b2.title)
