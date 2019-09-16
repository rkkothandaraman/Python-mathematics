S,X=map(int,input().split())
Count=0
while(S>=X):
    S=S-X
    Count=Count+1
print(Count)
