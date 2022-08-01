
count,result,prev=1,0,1

while ( count < 10 ):
    print(result, end = ' ' )
    result+=prev
    print(prev, end = ' ' )
    prev+=result
    count+=1
    
# 1 1 2 3 5 8 13 21 34 55