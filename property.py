##OKK
##class Test():
##    def __x1(self):
##        print("Boo")
##    def x2(self):
##        return self.__x1()
##
##x = Test()
##x.x2()
##
##x._Test__x1() PYTHON NAME MANGLING FOR DOUBLE UNDERSCORES

##OKK
##class C:
##    def __init__(self):
##        self._x = None
##
##    def getx(self):
##        return self._x
##
##    def setx(self, value):
##        self._x = value
##
##    def delx(self):
##        print("deleting x value")
##        del self._x
##
##    x = property(getx, setx, delx, "I'm the 'x' property.")
##
##c=C()
##c.x='1234'#invoke the setter
##print(c.x)#invoke the getter
##del c.x

#okkk
##class Parrot:
##    def __init__(self):
##        self._voltage = 100000
##
##    @property
##    def voltage(self):
##        """Get the current voltage."""
##        print( self._voltage )
##
##p=Parrot()
##p.voltage

##OKKK
##class Parrot:
##    def __init__(self):
##        self.v = 100000
##
##    @property
##    def voltage(self):#by default this is a getter
##        print("getter:")
##        print(self.v )
##
##p=Parrot()
##p.voltage


##OKKK
    
##class C:
##    def __init__(self):
##        self.a = None
##
##    @property #by default this is a getter)
##    def x(self):
##        print("Getting 'a' attribute:", self.a)
##        return self.a
##
##    @x.setter
##    def x(self, value):
##        self.a = value
##        print("Setting 'a' attribute:", self.a)
##
##
##    @x.deleter
##    def x(self):
##        del self.a
##        print("deleted")
##
##c1=C()
##c1.x=9#setter
##print(c1.x)#getter
##del c1.x#deleter
##del c1.x


class C:
    def __init__(self):
        self._a = None

    @property #by default this is a getter)
    def x(self):
        print("Getting 'a' attribute:", self._a)
        return self._a

    @x.setter
    def x(self, value):
        self._a = value
        print("Setting 'a' attribute:", self._a)


    @x.deleter
    def x(self):
        del self._a
        print("deleted")


c1=C()
c1.x=9 #setter
print(c1.x)#gettter
del c1.x#deleter
del c1.x
