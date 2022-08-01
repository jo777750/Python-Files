class d:
    

    def __del__(self):
        print( f"object {id(self)} got deleted")


print(id(d())== id(d()))# no references so object deleted as soon as its foundS








    
