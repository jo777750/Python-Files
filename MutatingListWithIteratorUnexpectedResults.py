text=list("earth sun")
combined=""
for ch in text:
    combined=combined+ch
    print("combined value:" + combined)
    print("ch value:" + ch)
    text.remove(ch)
    print("Now combined value:" + combined)

print(combined)
##text2=""
##text1=list("earth sun")
##text1.remove('e')
##text2+=text1[0]
##print("text1:" , text1)
##text1.remove('a')
##text2+=text1[0]
##print("text2:" , text2)
##
##print("text1:" , text1)
##text1.remove('r')
##text2+=text1[0]
##print("text2:" , text2)
##
##print("text1:" , text1)
##text1.remove('t')
##text2+=text1[0]
##print("text2:" , text2)
##
##print("text1:" , text1)
##text1.remove('h')
##text2+=text1[0]
##print("text2:" , text2)
##
##print("text1:" , text1)
##text1.remove(' ')
##text2+=text1[0]
##print("text2:" , text2)
##
##text1.remove('s')
##text2+=text1[0]
##print("text2:" , text2)
##
##
##
##text1.remove('u')
##text2+=text1[0]
##print("text2:" , text2)
##
##
##
##text1.remove('n')
##text2+=text1[0]
##print("text2:" , text2)







