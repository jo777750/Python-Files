import sys
res = 666**47
print(res)
res = list(map(int, str(res)))
i = 0
total = 0
while i < 133:
    total = total + res[i]
    print(str(total) + ',')
    i += 1

print('grand total:' + str(total))
sys.argv