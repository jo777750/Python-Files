student={'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25}
def test(student):
   new={'alok':30,'Nevadan':28}
   student.update(new)
   print("Inside the function",student)
   return
test(student)
print("outside the function:",student)