def AddNumbers(*args):
    result = 0
    for x in args:
        result += x
    return result

print(AddNumbers(1, 2, 3))
print(AddNumbers(10, 20, 30, 40))
print(AddNumbers(9, 2, 8, 4, 9))
print(AddNumbers(9, 2, 8, 4, 9, 99, 87, 46, 334))

print(10*'###')
#args is a tuple so following code is also ok

def AddNumbers(*bad_args):
    result = 0
    for x in bad_args:
        result += x
    return result

print(AddNumbers(1, 2, 3))
print(AddNumbers(10, 20, 30, 40))
print(AddNumbers(9, 2, 8, 4, 9))
print(AddNumbers(9, 2, 8, 4, 9, 99, 87, 46, 334))


