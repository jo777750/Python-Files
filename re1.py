import re
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
[w for w in words if re.search(r'tt', w)]
#['attempt', 'tattle']
[w for w in words if not re.search(r'tt', w)]
#['cat']
ip = 'They ate 5 apples and 5 oranges'
re.sub(r'5', 'FIVE', ip)
##'They ate FIVE apples and FIVE oranges'
re.sub(r'5', 'FIVE', ip,count=1)
##'They ate FIVE apples and 5 oranges'
re.sub(r'e', 'E', greeting)
##'HavE a nicE wEEkEnd'
re.sub('e', 'E', greeting)
##'HavE a nicE wEEkEnd'
line1 = 'start address: 0xA0, func1 address: 0xC0'
line2 = 'end address: 0xFF, func2 address: 0xB0'
bool(re.search(r'', line1))
##True
bool(re.search(r'', line2))
##True
bool(re.search(r'0xB0', line1))
##False
bool(re.search(r'0xA0', line1))
##True
foo='abc ABc ABC'
re.sub(r'abc', 'XYZ', foo,re.IGNORECASE)
#'XYZ ABc ABC'
re.sub(r'abc', 'XYZ', foo,flags=re.IGNORECASE)
#'XYZ XYZ XYZ'
foo='ABC ABc abc'
re.sub(r'abc', 'XYZ', foo,re.IGNORECASE)
#'ABC ABc XYZ'
re.sub(r'abc', 'XYZ', foo,flags=re.IGNORECASE)
items
['goal', 'new', 'user', 'sit', 'eat', 'dinner']
[w for w in items if re.search(r'a',w) or re.search(r'w',w)]
['goal', 'new', 'eat']
[w for w in items if re.search(r'e',w) and re.search(r'n',w)]
['new', 'dinner']
[w for w in items if re.search(r'a|w',w)]#used | OR operator      
['goal', 'new', 'eat']



