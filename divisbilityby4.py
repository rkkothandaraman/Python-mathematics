N=input()
if(len(N)>=1 and len(N)<=1000):
    M=int(N)
    if(M and M%4==0):
        print("YES")
    else:
        print("NO")
