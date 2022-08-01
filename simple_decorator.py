####def my_decorator(func):
####    def wra():
####        print("Something is happening before the function is called.")
####        func()
####        print("Something is happening after the function is called.")
####    return wra
####
####def say_whee():
####    print("Whee!")
####
####say_whee=my_decorator(say_whee)
####print(type(say_whee))
####say_whee()
##
##output:
##Something is happening before the function is called.
##Whee!
##Something is happening after the function is called.
##
#####################
###now use @(annotation) symbol
##
##def my_decorator(func):
##    def wrapper():
##        print("Something is happening before the function is called.")
##        func()
##        print("Something is happening after the function is called.")
##    return wrapper
##
##@my_decorator
##def say_whee():
##    print("Whee!")
##
##say_whee()
##
##
##output:
##Something is happening before the function is called.
##Whee!
##Something is happening after the function is called.

###################


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        func()

        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

##OUTPUT:
##Something is happening before the function is called.
##Whee!
##Whee!
##Something is happening after the function is called.




    
