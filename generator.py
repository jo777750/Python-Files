def g():
    print("inside generator")
    yield 10

    
type(g())
#<class 'generator'>
g()
<generator object g at 0x0000023D2B7BFED0>
f()
#something
z=g()
z
#<generator object g at 0x0000023D2B8B2650>

for i in z:
    print(i)

    
#inside generator
#10
for i in z:
    print(i)

    
#further nothing...............
