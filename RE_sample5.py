import re
with open(r"C:\Users\JAISIMHA\Documents\GitHub\jo777750.github.io\a.txt") as f:
    for line in f:
        print("found:", re.search('^[^r]', line))
  #      print("found:", re.search('(?<=abc)', line))
  
'''  
@
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
'''

'''
found: <re.Match object; span=(0, 1), match='@'>
found: <re.Match object; span=(0, 1), match='s'>
found: <re.Match object; span=(0, 1), match="'">
found: <re.Match object; span=(0, 1), match='p'>
found: <re.Match object; span=(0, 1), match='w'>
found: None
found: <re.Match object; span=(0, 1), match='"'>
found: <re.Match object; span=(0, 1), match='p'>
found: <re.Match object; span=(0, 1), match="'">
found: <re.Match object; span=(0, 1), match='p'>
found: <re.Match object; span=(0, 1), match='w'>

C:\Program Files (x86)\Notepad++>

'''

