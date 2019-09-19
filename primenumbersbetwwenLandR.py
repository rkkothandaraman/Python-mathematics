L,R=map(int,input().split())
count=0
p=[]
for i in range(L,R+1,1):
    count=0
    for k in range(2,i):
        if(i%k==0):
            count=count+1
    if(count==0):
        p.append(i)
maxcounter=len(p)
print(maxcounter)

        
