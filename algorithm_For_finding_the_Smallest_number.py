N=int(input())
li=list(map(int,input().split()))
min=li[0]
if(len(li)==N):
    for i in range(N):
        if li[i]<min:
            min=li[i]
    print(min)
