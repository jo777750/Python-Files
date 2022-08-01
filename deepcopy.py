# #shallow copy:
# A=[10,20,40]
# b=A
# b
# [10, 20, 40]
# A
# [10, 20, 40]
# b.append(9)
# b
# [10, 20, 40, 9]
# A
# [10, 20, 40, 9]

# # deep copy;;
# a
# [1, 2, 3]
# b=a[:]
# b
# [1, 2, 3]
# b.append(9)
# b
# [1, 2, 3, 9]
# a
# [1, 2, 3]

k=[1,2,3]

a=k[0:1:1]
print("a=",a)
print("k=",k)
print("a=",a)

