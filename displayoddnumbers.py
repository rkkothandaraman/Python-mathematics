M=input()
new=[]
count=0
N=[int(x) for x in M]
for i in N:
    if (i%2!=0):
        count=count+1
        new.append(i)
for  x in new:
    print(x, end=" ")
if(count==0):
    print("-1")

