x=[7, 8, ['kkk', 77777, 888]]
# INSERT AT 4TH PLACE
x.insert(3,"kk")
print(x)
# INSERT AT 3D PLACE
x.insert(2,"JUNGLE")
print(x)

#format extend(iterable)
x.extend(range(7))
print(x)

y=[3,6]
x.extend(y)
print(x)

set1={'april','may'}
tuple1=('monday','sunday')
x.extend(set1)#extend set
x.extend(tuple1)#extend tuple

print(x)

g=[666,777]
h=[111,222]


print(h+g)


import dis
def demo():
    x=[91,72]
    x+=[30]
    return x
dis.dis(demo)




a = [1, 2]
b = [3, 4]

a[len(a):] = b #####################SLICE OPERATOR


# Output: [1, 2, 3, 4]
print('a =', a)