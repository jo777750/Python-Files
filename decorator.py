import sys

from functools import  lru_cache

print(sys.argv)

print("number is ",sys.argv[1])
@lru_cache
def is_prime(number):
    for n in range(2, number//2):
        if number % n == 0:
            return(print("not prime number"))
        else: 
            return(print(" prime number"))
     

is_prime(int(sys.argv[1]))