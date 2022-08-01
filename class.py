class C:
    def xyz():
        print("method called!")

c = C()
c.xyz

=================

>>> from keyword import iskeyword

>>> 'hello'.isidentifier(), iskeyword('hello')
(True, False)
>>> 'def'.isidentifier(), iskeyword('def')
(True, True)