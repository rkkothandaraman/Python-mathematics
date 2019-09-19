L,H,W=map(int,input().split())
Surface=L*H+H*W+L*W
volume= L*H*W
print(2*Surface,volume)
