##>>> "jjcjfkkrmc"[15:2]
##''
##>>> "jjcjfkkrmc"[15::2]
##''
##>>> "jjcjfkkrmc"[1::2]
##'jjkrc'
##>>> "abcdefgh"[1::2]
##'bdfh'
##>>> s=[1,2,3,4,5,6,7,8]
##>>> s[1:8:1]
##[2, 3, 4, 5, 6, 7, 8]
##>>> s[0:8:1] #0 is starting of slice
##[1, 2, 3, 4, 5, 6, 7, 8]
##>>> s[0:8:2]
##[1, 3, 5, 7]
##>>> s[0::2]
##[1, 3, 5, 7]


def even_or_odd(num):
    return "eovdedn"[num % 2 :: 2]
print(even_or_odd(1))
print(even_or_odd(30))

