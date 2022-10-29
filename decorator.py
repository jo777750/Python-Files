import sys

from functools import  lru_cache

print(sys.argv)
file = open('geek.txt', 'w+')
file.write('This is a test ggggS')
#print("number is ",sys.argv[1])
@lru_cache

def is_prime(number):
    global x
    for n in range(2,int(sys.argv[1])):
            for x in range(2,n):
                
                if n % x == 0:
                                   
                    print(f"{n} not a prime number:")
                    break
            else:
                print(f"{n}  a prime number:")

              

            
is_prime(int(sys.argv[1]))