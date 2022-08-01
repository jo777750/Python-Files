@my_decorator
def my_function():
    print("Hi")
type(my_function())
def my_function():
    print("Hi")

my_function = my_decorator(my_function)
type(my_function())
