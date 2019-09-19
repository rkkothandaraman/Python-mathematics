import math
x,y=map(int,input().split())
count=0
for i in range(x,y+1):
    m=math.sqrt(i)
    if(m**2==i):
        count=count+1
print(count)
