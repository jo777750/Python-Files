
count,result,prev=1,0,1

for i in range(10):
    print(result, end = ' ' )
    result+=prev
    print(prev, end = ' ' )
    prev+=result
    
# 1 1 2 3 5 8 13 21 34 55