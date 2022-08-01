def x():
    a=[4,6,8,9,10]
    a[0]=9
    print(a)

    
x()
#print(a)#a not defined as function stack gone

b=[10,20,30,40,50]

def y():
    b[0]=45
    print("after modifing b function:", b)

y()
print("after exiting from  function:", b)

b=[10,20,30,40,50]

def y(b):
    b[1]=85
    print("after modifing b function:", b)

y(b)
print("after exiting from  function:", b)

