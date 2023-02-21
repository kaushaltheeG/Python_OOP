from dataclasses import dataclass

@dataclass(frozen=True) #frozen makes the class attributes immuntable in and outside of the class 
class ImmutableClass: 
    value1: str = "value 1"
    value2: int = 0

    def somefunc(self,newval): #throws FrozenInstanceError because it is immutable 
        self.value2 = newval


obj = ImmutableClass()
print(obj)
# obj.value2 = 1 #throws FrozenInstanceError because it is immutable 
obj.somefunc(1)