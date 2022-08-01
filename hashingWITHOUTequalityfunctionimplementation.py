#!/usr/bin/env python

class User:

    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation

u1 = User('John Doe', 'gardener')
u2 = User('John Doe', 'gardener')

print('hash of user 1')
print(hash(u1))

print('hash of user 2')
print(hash(u2))

if (u1 == u2):
    print('same user')
else:
    print('different users')