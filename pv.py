student={'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25}
def test(student):
   new={'alok':30,'Nevadan':28}
   student.update(new)
   print("Inside the function",student)
   return
test(student)
print("outside the function:",student)
del student
#list
student=[28,25,32,25]
def test(student):
   d=[6,999]
   student.extend(d)
   print("list:Inside the function",student)
   return
test(student)
print("list:outside the function:",student)
del student

#tuple
# student=(28,25,32,25)
# def test(student):
   # d=(6,999)
   # student.extend(d)
   # print("list:Inside the function",student)
   # return
# test(student)
# print("list:outside the function:",student)
#del student

#set
student={28,25,32,25}
def test(student):
   
   student.add(6)
   print("set:Inside the function",student)
   return
test(student)
print("set:outside the function:",student)