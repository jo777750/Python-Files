class y(int):#y is a subclassof int
    
    def __ge__(self,a):#sub class'y' defines its own ge method , overriding base class 'ini
        print("Inside ge Dunder")
        print(super().__ge__(a))
        
        
z=y(78)
z>=5

class k(str):
    pass
k1=k(25)
print(k1)
print(type(k))
