n the third example, we implement the __eq__ and the __hash__ methods.

custom_object3.py
#!/usr/bin/env python

class User:

    def __init__(self, name, occupation):

        self.name = name
        self.occupation = occupation

    def __eq__(self, other):

        return self.name == other.name \
            and self.occupation == other.occupation

    def __hash__(self):
        return hash((self.name, self.occupation))

    def __str__(self):
        return f'{self.name} {self.occupation}'


u1 = User('John Doe', 'gardener')
u2 = User('John Doe', 'gardener')

users = {u1, u2}

print(len(users))

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}')
else:
    print('different users')

print('------------------------------------')

u1.occupation = 'programmer'

users = {u1, u2}

print(len(users))

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}')
else:
    print('different users')