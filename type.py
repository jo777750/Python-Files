    
def g():
    print("inside generator")
    yield 1

    
z=g()

def wrap():
    for i in z:
        pass

        
print(type(g()))

print(type(wrap()))
print("end of 1st wrap")
print(type(g()))

print(type(wrap()))
print("end of 2nd wrap")
print(type(g()))

print(type(wrap()))
print("end of 3rd wrap")
print("lambda")

type(lambda a:None)

print(type(type))#output:class 'type'

