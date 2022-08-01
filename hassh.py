x=[1,2]
hash(x)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    hash(x)
TypeError: unhashable type: 'list'
x={1,2}
hash(x)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    hash(x)
TypeError: unhashable type: 'set'
x=(4,5)
hash(x)
-1009709641759730766
d={'a':1}
d
{'a': 1}
hash(d)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    hash(d)
TypeError: unhashable type: 'dict'
