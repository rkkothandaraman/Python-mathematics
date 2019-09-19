S,X=map(int,input().split())
li1=[]
li2=[]
li3=[]
for i in range(1,S+1):
        if(S%i==0):
            li1.append(i)
for j in range(1,X+1):
    if(X%j==0):
        li2.append(j)
li3=set(li1)& set(li2)
if(len(li3)>1):
    print("0")
else:
    print("1")
