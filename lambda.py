def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(0))
print(f(1))

# lambda arguments : expression
# The expression is executed and the result is returned:
def myfunc(n):
    return lambda a : a * n

print(type(myfunc(2)))


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler)
print(mytripler)


print(mydoubler(11))
print(mytripler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


x = lambda a, b : a * b
print(x(5, 6))



def a(n):
    return 5 * n
a(34)
print(type(a))


class c:
    def xset():
        print(type(xset))
        print(type(xset()))

print(type(c))

c1=c()
print(type(c1))



