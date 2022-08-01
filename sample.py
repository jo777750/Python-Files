# import datetime
# print("hi")
# today = datetime.datetime.now()
# str(today)
# repr(today)


s="""w'o"w"""
repr(s)
'\'w\\\'o"w\''
str(s)
'w\'o"w'
print(repr(s))
'w\'o"w'
print(str(s))
w'o"w
s="""w'o"""
repr(s)
'"w\'o"'
str(s)
"w'o"
print(repr(s))
"w'o"
print(str(s))
w'o
s=""""""w'o"""""
SyntaxError: unterminated string literal (detected at line 1)
s="""w"""
s
'w'
str(s)
'w'
print(s)
w
repr(s)
"'w'"
print(repr(s))
'w'
print(str(s))
w
