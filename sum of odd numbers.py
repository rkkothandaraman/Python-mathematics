X,Y=map(int,input().split())
sum=0
for i in range(X,Y+1,1):
    if i%2!=0:
        sum=sum+i
print(sum)
    
