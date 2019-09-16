N=int(input())
S=[int(m) for m in input().split()]
max=S[0]
count=0
index=0
if(len(S)==N):
    for i in range(N):
        if(max<S[i]):
            index=i
            count=count+1
    if(count==1):
        print(index)
    else:
        print(-1)
