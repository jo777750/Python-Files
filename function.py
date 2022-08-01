def foo(a,b, /,fname='jay', *,lname='simha'):
    print (a,b,fname,lname)
    
#foo(2)#TypeError: foo() missing 1 required positional argument: 'b'

# you cant pass positional only with a keyword
# you cant pass positional after a keyword
# you cant omit the keyword for keyboard only arguements

foo(2,4)
foo(2,4,'abc')
foo(2,4,'abc','xyz')#TypeError: foo() takes from 2 to 3 positional arguments but 4 were given
#so change to below

foo(2,4,'abc',lname='xyz')

foo(4,'abc','xyz')

foo(4,'abc')

foo('abc','xyz')

#foo('xyz') #TypeError: foo() missing 1 required positional argument: 'b'

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    # print("-- This parrot wouldn't", action, end=' ')
    # print("if you put", voltage, "volts through it.")
    # print("-- Lovely plumage, the", type)
    # print("-- It's", state, "!")
    
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# As guidance:

# Use positional-only if names do not matter or have no meaning, and there are only a few arguments which will always be passed in the same order.
# Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names.