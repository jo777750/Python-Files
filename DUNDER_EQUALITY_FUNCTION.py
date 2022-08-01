#n the third example, we implement the __eq__ and the __hash__ methods.


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
#u1 and u2 are equal so length of the users set is 1 
print(len(users))
breakpoint()
print(hash(u1))
print(hash(u2))
#same hash values as objects are equal
if (u1 == u2):
    print("same  users")
    print(f'{u1} == {u2}')
else:
    print('different users')


if (u1.__eq__(u2) == True ):
    print("same DUNDER Function users")

print('------------------------------------')

u1.occupation = 'programmer'

users = {u1, u2}

print(len(users))
#u1 and u2 are different so length of the users set is 2 

if (u1 == u2):

    print(f'{u1} == {u2}')
else:
    print('different users')
    #same hash values as objects are equal

#-------------

if (u1.__eq__(u2) == True ):
    print("same users")
else:
    print('different users')

print(hash(u1))
print(hash(u2))
print("different DUNDER Function users")
