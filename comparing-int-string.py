
#see gg.py
def chk2():

    secret_number = 7

    guess = int(input("What number am I thinking of? "))
    print(guess)
    print(type(guess))
    print(secret_number)
    print(type(secret_number))

    if secret_number == guess:
        print("Yay! You got it!")
    else:
        print("No, that's not it.")
        
def chk3():
       print("hi mister")
       
       
def chk4(fname):
    print("goodbye,", fname )


if __name__ == "__main__":
    import sys
    chk4(sys.argv[1])        
        

