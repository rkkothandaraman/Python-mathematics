def factorial(N):
    if (N==0):
        return 1
    else:
        Fact=1
        for i in range(N,1,-1):
            Fact=Fact*i
        return Fact
N,K=map(int,input().split())
if(N>K):
    Y=N-K
    a=factorial(N)
    b=factorial(Y)
    output=a/b
    print(int(output))