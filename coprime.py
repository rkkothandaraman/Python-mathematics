S,X=map(str,input().split())
M=len(S)
Y=len(X)
li1=[]
li2=[]
li3=[]
for i in range(1,M+1):
        if(M%i==0):
            li1.append(i)
for j in range(1,Y+1):
    if(Y%j==0):
        li2.append(j)
li3=set(li1)& set(li2)
if(len(li3)>1):
    print("no")
else:
    print("yes")
