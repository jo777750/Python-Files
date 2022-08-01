'''
FOR SIMPLE LIST COPY OUTPUT LOOKS DIFFERENCE THAN THE NESTED LIST BUT INTERNALLY OBJECTS PLAY DIFFERENTLY The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances) 

import copy
# nested list
a=[7, 8, ['kkk', 77777]]
b=copy.copy(a)
b[2].append(888)
print("a is:",a)
print("b is:",b)
print(id(a))
print(id(a[0]))
print(id(a[1]))
print("-------------")
print(id(b))
print(id(b[0]))
print(id(b[1]))
#simple list
x=[1,2]
y=copy.copy(x)
y.append(9)
x.append(7779)
print("x is:",x)
print("y is:",y)
print(id(x))
print(id(x[0]))
print(id(x[1]))
print(id(y))
print(id(y[0]))
print(id(y[1]))
print(id(y[2]))
m=[5,6]
n=copy.deepcopy(m)
n.append(788)
print("m is:",m)
print("n is:",n)
print(id(m[0]))
print(id(m[1]))
print("--------")
print(id(n[0]))
print(id(n[1]))
print(id(n[2]))
a is: [7, 8, ['kkk', 77777, 888]]
b is: [7, 8, ['kkk', 77777, 888]]
2108632336896
2108626174384
2108626174416
-------------
2108632337216
x is: [1, 2, 7779]
y is: [1, 2, 9]
2108632314176
2108626174192
2108626174224
2108632315456
2108626174448
m is: [5, 6]
n is: [5, 6, 788]
2108626174320
2108626174352
--------
2108662081712