##def make_incrementor(n):
##    return lambda x: x + n
##f = make_incrementor(42)
##print(f(0))
##print(f(1))


##def make_incrementor(n):
##    return  x + n
##f = make_incrementor(2)
##print(f)

def myfunc(n):
    return lambda a : a * n

print(myfunc(2))
print(myfunc(3))

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



