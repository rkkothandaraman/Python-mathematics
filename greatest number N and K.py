S,X=map(int,input().split())
li1=[]
li2=[]
li3=[]
if(X <= 10000 and S<=10000):
    for i in range(1,S+1):
        if(S%i==0):
            li1.append(i)
    for j in range(1,X+1):
        if(X%j==0):
            li2.append(j)
    li3=set(li1)& set(li2)
    N=max(li3)
    print(N)
